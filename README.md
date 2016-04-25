
# MKR

## Session One: Kick-Off

24.4.2016

### Core System Requirements

* test-driven
* add-remove components
* exchange components
* documentation(simple)
* one-click-deploy
* 12 Factors (http://12factor.net/)

### Results:

We use a iterative work process with the following phases:

1. **Plan** the iteration and decide on a test
2. **Develop** whatever there is to develop
3. **Run in Operations** using a one-click installer
4. **Test** the test decided previously
5. **Document** in README.md

All components interact with a *git repository*.


## Session Two: Hello World

### Goal:

A server running a Hello World web app.

### Technologies used:

* Github repo
* Docker
* Django
* Selenium
* virtualenv

### Results

* tests work
* Docker container created with a single script (Dockerfile)
* TODO: https://docs.docker.com/compose/django/

### Notes

* make sure to use compatible versions of Selenium/Firefox
* make sure you do not use Python2 on one dev machine and Python3 on the other
* do not try `yes | sudo apt-get install docker`

