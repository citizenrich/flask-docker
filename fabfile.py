from fabric.api import *

env.hosts = ['tracpro.org']
env.user = 'root'
repo = '~/Dropbox/Code/flask-docker'

def prep():
    with lcd(repo):
        local('git add -A')
        local('git commit -m "fabfile auto-commit"')
        local('git push -u origin master')

def install():
    run('apt-get -qqy update')
    run('apt-get -qqy install git docker')

def update():
    run('apt-get -qq update')
    run('apt-get -qqy upgrade')


def deploy():
    with cd('/etc/init'):
        env.warn_only = True
        run('service nginx restart')
