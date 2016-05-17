
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

* created Django instance + application via Docker
* docker-compose up creates an image, installs django, attaches local filesystem and starts the server
* the tests passes

### Notes

* Docker is under heavy development. Make sure you have the latest version, so that the documentation corresponds to your system.
* Docker installation instructions worked nicely
* strange phenomenon on KR's machine: reboot, after the reboot terminals did not start, pressing Ctrl-C resulted in a Python error message connected to virtualenv (maybe because leftovers from previous virtualenv session(s)?? Docker took a long while to start after installation, much longer than on MRs machine.
* it took a while to figure out how to create a Django app in the right folder via docker-compose (with the -w option). It is a bit annoying that files created by docker-compose all belong to 'root'.


## Session Four: Postgres

1.5.2016

### Goal

* Add a Postgres database that keeps a table with quotes
* Quotes from the database are highlighted on the web page

### Results

* added example quotes by Sun Tzu and test
* added postgres container to docker-compose
* added model, created a migration via docker-compose
* added a view and HTML template to display quotes
* created a data entry manually in a django shell session
--> works

### Notes

* does not pass the one-click test yet, because we wrote the data entry manually
* found that docker containers tend to accumulate. You can clean them up with:

    docker ps -a | grep 'weeks ago' | awk '{print $1}' | xargs --no-run-if-empty docker rm

    docker ps -a | awk '{print $1}' | xargs --no-run-if-empty docker rm


## Session Five: Service Health Check

16.5.2016

### Goal

* more smooth startup according to one-click paradigm

### Results

* problem re-occured: when we start docker-compose so that new containers are created, the process fails because postgres creation is overtaken by Django --> Django doesn't find database because it is not ready yet.
* problem solved brute-force by sleeping 10 seconds in container before starting Django
* for more elegant solution wrote shell script that starts services via docker-compose one by one
* added "service health check": shell script on Django container waits for DB to come up

### Notes

* learned what a 'race condition' is
* the health check could possibly hang in an endless loop if DB server crashes, therefore not too advisable for production


## Session Six: Fixtures

17.5.2016

### Goal

* build a test that passes without manually adding a DB entry.

### Results

* added test for views in django application
* used ORM for adding test data
* used docker-compose to run the test inside the container
* extended shell script to stop containers if tests fail

### Notes

* three independent sources recommend not using JSON fixtures, but use the ORM or tomboy instead.
* problem: how to write a test fixture that runs inside the Django container when the test runs locally? 
* the start_docker.sh script removes *all* containers on the local machine!


## NEXT

* create fixtures in containver via management command that is used via fabric
* add Django admin interface
* make template/view for quotes nicer
* add manage command
