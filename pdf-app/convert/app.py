import os
import logging
import traceback
from threading import RLock
from flask import Flask, request, send_file
from tempfile import mkstemp
from werkzeug.wsgi import ClosingIterator
from werkzeug.exceptions import HTTPException
from pantomime import FileName, normalize_mimetype, mimetype_extension
from subprocess import call

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('convert')
lock = RLock()


class ShutdownMiddleware:
    def __init__(self, application):
        self.application = application

    def post_request(self):
        if app.is_dead:
            os._exit(127)

    def __call__(self, environ, after_response):
        iterator = self.application(environ, after_response)
        try:
            return ClosingIterator(iterator, [self.post_request])
        except Exception:
            traceback.print_exc()
            return iterator


app = Flask("convert")
app.is_dead = False
app.wsgi_app = ShutdownMiddleware(app.wsgi_app)



@app.route("/convert", methods=['POST'])
def convert():
    if app.is_dead:
        return ("DEAD", 500)
    upload_file = None
    acquired = lock.acquire(timeout=1)
    if not acquired:
        return ("BUSY", 503)
    try:
        timeout = int(request.args.get('timeout', 100))
        for upload in request.files.values():
            file_name = FileName(upload.filename)
            mime_type = normalize_mimetype(upload.mimetype)
            if not file_name.has_extension:
                file_name.extension = extensions.get(mime_type)
            if not file_name.has_extension:
                file_name.extension = mimetype_extension(mime_type)
            fd, upload_file = mkstemp(suffix=file_name.safe())
            os.close(fd)
            log.info('PDF convert: %s [%s]', upload_file, mime_type)
            upload.save(upload_file)
            log.info('About to begin conversion.')
            call('libreoffice --headless --convert-to pdf --outdir %s %s ' %
            	('/tmp/', upload_file), shell=True)
            return send_file('/tmp/output.pdf',
                             mimetype='application/pdf',
                             attachment_filename='output.pdf')
        return ('No file uploaded', 400)
    except HTTPException:
        raise
    except ConversionFailure as ex:
        app.is_dead = True
        return (str(ex), 400)
    except Exception as ex:
        app.is_dead = True
        log.error('Error: %s', ex)
        return ('FAIL', 503)
    finally:
        if upload_file is not None and os.path.exists(upload_file):
            os.unlink(upload_file)
        if os.path.exists('/tmp/output.pdf'):
            os.unlink('/tmp/output.pdf')
        lock.release()
