
# Table of Contents

1.  [Setting the scene](#orgedfe2d9)
    1.  [Introductions](#orgc0df5c4)
    2.  [Rules of engagement](#org31fa34e)
    3.  [Demonstration of literate programming](#org424e66c)
    4.  [Questions before we begin](#org1cab783)
2.  [Starting our adventure](#orgc61a246)
3.  [Looking up what cloud native means](#org07a8409)
    1.  [Dive right into the code](#org6510678)
4.  [Kubernetes?](#org2291f11)

Welcome to the first ANZ Cloud Native Bootcamp for 2020! 


<a id="orgedfe2d9"></a>

# TODO Setting the scene


<a id="orgc0df5c4"></a>

## TODO Introductions

Firstly some quick introductions, my name is James Blair. I'm an Automation Lead at ANZ New Zealand based in Wellington. I've been in the tech industry for eight years, most of that working within government at Inland Revenue and joined ANZ a year ago.

To introduce this session, I first want to go back to a particular, nostalgic memory of my childhood which is reading Goosebumps choose your own adventure novels by R.L. Stine. We all remember these right?

![img](./images/goosebumps.jpg)

Ok so rest assured my goal for the session today isn't to scare you! However I am hoping we can go on something like an adventure, as we explore cloud native together, so what I've done is set this workshop up in a choose your own adventure style.

Depending on the choices you make within the adventure we'll focus primarily on either [docker](https://docker.com) or [kubernetes](https://kubernetes.io).


<a id="org31fa34e"></a>

## TODO Rules of engagement

Before we begin, for this style of workshop to run smoothly, we need to cover some key messages:

-   **Everyone participates** - At each step of this adventure, we all need to collectively vote on the next step we take. To do that we'll be using the polls feature in zoom. Let's test that now to ensure it works for everyone. Additionally as we progress through our journey there will be opportunities to get hands on.

-   **Asking questions** - The aim of this session is to be as interactive as possible, please don't hold questions to the end, I'm happy to answer questions as we go :)

-   **Resources** - All materials from this workshop will be publicly available on my gitlab and a link provided in chat at the end of our session.

-   **Technology** - For demonstrations and hands on segments we will always be working as one group. To navigate through our adventure and run code we'll be using a technique called [literate programming](https://en.wikipedia.org/wiki/Literate_programming) which for some quick history was formed by Donald E. Knuth in 1984. Essentially what this involves is using a development environment such as `emacs` with `org-mode` to weave our adventure and choices into the flow of processes and code we work through. Additionally we'll be using a tool called `tmate` which will allow us to all pair together and share the same development environment and terminals. I've taken to calling what we'll be doing today ***literate pair programming***.


<a id="org424e66c"></a>

## TODO Demonstration of literate programming

I'm going to change my screen layout now in Zoom so you can see what I call our pairing "left eye" and "right eye" which are just terminals. The left eye runs our `emacs` development environment. The right eye is the terminal we will be actually running our commands and code in.

Let's take this opportunity to test connectivity with `tmate`.  Can you all please:

-   Open two new browser windows and arrange them side by side
-   Navigate to the left eye <https://tmate.io/t/x>
-   Navigate to the right eye <https://tmate.io/t/x>
-   In the right eye type `echo [your first name]`


<a id="org1cab783"></a>

## TODO Questions before we begin

Again before we start our journey, does anyone have any questions or have any issues connecting with `tmate`?


<a id="orgc61a246"></a>

# TODO Starting our adventure

So here you are, a week into a new Summer of Tech internship at ANZ and you've been assigned to one of our cloud squads. You've been tasked with helping to migrate an internal application into a scalable cloud native service that can be run on a public cloud provider such as Google or AWS.

The application in question is a basic two tier phone directory app made up of a web server and a database, currently running on a virtual machine on premise.

You've been given freedom on how to approach the task do you&#x2026;

-   [1 - Start by looking up what "cloud native" means](#org07a8409)
-   2 - Start by reviewing the existing application

<details>
<summary>HINT</summary>

****Nice work, you just revealed a hint!****
</details>


<a id="org07a8409"></a>

# TODO Looking up what cloud native means

You make a start by looking up what "cloud native" means, finding your way to the [definition](https://github.com/cncf/toc/blob/master/DEFINITION.md) approved by the [Cloud Native Computing Foundation](https://www.cncf.io/) in 2018:

> "Cloud native technologies empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach.
> 
> These techniques enable loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil.
> 
> The Cloud Native Computing Foundation seeks to drive adoption of this paradigm by fostering and sustaining an ecosystem of open source, vendor-neutral projects. We democratize state-of-the-art patterns to make these innovations accessible for everyone."

A wordy official definition, so from my perspective, when I'm talking about cloud native computing generally what we're talking about is code that runs in [docker](https://www.docker.com/) containers, is orchestrated by [kubernetes](https://kubernetes.io/) and runs on a public cloud provider like Google or Amazon Web Services.

Now that you've had a look at what cloud native means, 


<a id="org6510678"></a>

## Dive right into the code


<a id="org2291f11"></a>

# TODO Kubernetes?

Testing

