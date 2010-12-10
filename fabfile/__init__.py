"""
This is really just another example fab file, you'll need to edit it to make it work
for your environment, as well as the fabfile/env.py file. To do so, just change the
paths specified here, and write the appropriate command to restart your web serving app.
"""
from fabric.api import run

from fabfile.env import ideas

#set environment
config = ideas()

def git_pull():
    run("cd /var/www/ideas/; git pull %s %s" % (config['parent'], config['branch']))

def git_reset(hash):
    ''' 
    Usage: fab git_reset:hash
    '''
    run("cd /var/www/ideas/; git reset --hard %s" % hash)

def restart_uwsgi():
    '''
    Restart the web server on this machine.
    '''
    run("sudo /usr/local/etc/rc.d/uwsgi restart")

def rmpyc():
    '''
    Remove all .pyc files in the directory.
    '''
    run("cd /var/www/ideas/; find . -name '*.pyc' -exec rm {} \;")

def deploy():
    git_pull()
    rmpyc()
    restart_uwsgi()
