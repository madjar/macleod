from fabric.api import local

def epio(commandstring):
    local("epio {0}".format(commandstring))

def deploy():
    epio('upload')
    epio('django syncdb')
    epio('django migrate')