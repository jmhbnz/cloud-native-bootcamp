# Base standard python three image
FROM python:3-alpine

# Install and configure packages
RUN apk add libreoffice \
  build-base \
  msttcorefonts-installer \
  py3-lxml \
  fontconfig && \
  update-ms-fonts && \
  fc-cache -f

# Set a directory to work from
WORKDIR /tmp

# Copy the python package requirements in
COPY requirements.txt /tmp/

# Install python package requirements with pip
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copy application code and setup 
COPY convert /tmp/convert

# Suggest a port to be exposed
EXPOSE 3000

# Run the python web server
CMD ["gunicorn", \
     "--threads", "3", \
     "--bind", "0.0.0.0:3000", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "--timeout", "600", \
     "--graceful-timeout", "500", \
     "convert.app:app"]

