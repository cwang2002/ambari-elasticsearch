import sys, os, pwd, signal, time
from resource_management.core.exceptions import ComponentIsNotRunning
from resource_management import *
from subprocess import call
from docker import Client
from datetime import datetime
import cmd, traceback
from __main__ import traceback

class Elasticsearch(Script):
  cli = Client(base_url='unix://var/run/docker.sock')

  def install(self, env):
    print "install"
    import params
    env.set_params(params)
    print "pull docker image"
    cmd = format("docker pull {dockerImage}")
    print cmd
    Execute(cmd)

  def configure(self, env):
    print "configure"

  def start(self, env):
    print "start"
    import params
    env.set_params(params)
    print "start docker container"
    #cmd = format("docker run -d --name {containerName} -p 80:80 {dockerImage}")
    #print cmd
    #Execute(cmd)
    Elasticsearch.cli.start(container=params.containerName)


  def stop(self, env):
    print "stop"
    import params
    env.set_params(params)
    print "stop docker container"
    Elasticsearch.cli.stop(container=params.containerName)

  def status(self, env):
    print "status"
    import params
    env.set_params(params)
    print str(datetime.now())+":check docker container status"
    #cmd = format("docker inspect {containerName} | grep running")
    try:
        container = Elasticsearch.cli.inspect_container('drs-search')
        isRunning = container['State']['Running']
        print isRunning
        if isRunning == False:
            raise ComponentIsNotRunning()
    except Exception, e:
        traceback.print_exc()
        raise ComponentIsNotRunning()

if __name__ == "__main__":
  Elasticsearch.execute()
