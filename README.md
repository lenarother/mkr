
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

* git repo initialized (lenarother/mkr)
* virtualenv set up
* test works and fails
* Docker container created with a single script (Dockerfile)

### Notes

* make sure to use compatible versions of Selenium/Firefox
* make sure you do not use Python2 on one dev machine and Python3 on the other
* do not try `yes | sudo apt-get install docker`


## Session Three: One-Click

30.4.2016

### Goals

* get Docker to run by `start_docker.sh` 

### Results

* docker-compose installs django

### Notes

* Docker is under heavy development. Make sure you have the latest version, so that the documentation corresponds to your system.
* Docker installation instructions worked nicely
* strange phenomenon on KR's machine: reboot, after the reboot terminals did not start, pressing Ctrl-C resulted in a Python error message connected to virtualenv (maybe because leftovers from previous virtualenv session(s)?? Docker took a long while to start after installation, much longer than on MRs machine.
