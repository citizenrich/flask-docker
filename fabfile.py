from fabric.api import *

env.hosts = ['tracpro.org']
env.user = 'root'
repo = '~/Dropbox/Code/flask-docker'
#home = '/home/admin'
#app = '/home/admin/flask-docker/app'

def prep():
    with lcd(repo):
        local('git add -A')
        local('git commit -m "fabfile auto-commit"')
        local('git push -u origin master')

def install():
    run('apt-get -qqy update')
    run('apt-get -qqy install git docker') #removed supervisor

def update():
    run('apt-get -qq update')
    run('apt-get -qqy upgrade')


def deploy():
    with cd('/etc/init'):
        env.warn_only = True
        run('start telephony') #for upstart
        run('restart telephony') #for upstart
        run('service nginx restart')
        #run("ps -ef | grep 'gunicorn' | grep -v grep | awk '{print $2}' | xargs kill -9")
        #run('gunicorn -b 127.0.0.1:8000 --workers=5 -m 007 wsgi')
