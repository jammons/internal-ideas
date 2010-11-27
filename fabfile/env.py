from fabric.api import env

def ideas():
    '''
    env.hosts (list) of hosts to deploy to
    env.shell (str) to path of bash - on FreeBSD you'll want "usr/local/bin/bash -l -c"
    env.user (str) ssh username
    env.password (st) ssh password
    '''

    #git setup
    config = {}
    config['parent'] = 'origin'
    config['branch'] = 'master'

    return config
