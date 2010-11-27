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
