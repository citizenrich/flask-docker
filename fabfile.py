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
    run('wget -qO- https://get.docker.com/ | sh')
    run('apt-get -qqy install git')

def update():
    run('apt-get -qq update')
    run('apt-get -qqy upgrade')

def clone():
    with cd('/root'):
        env.warn_only = True
        run('rm -rf flask-docker')
        sudo('git clone -q https://github.com/citizenrich/flask-docker.git', user='admin')

def whatsup():
    run('docker ps -l')

def image():
    with cd('/root/flask-docker'):
        env.warn_only = True
        run('docker build -t test .')

def docker():
    with cd('/root/flask-docker'):
        run('docker run --name test_instance -i -t test')

#debconf: delaying package configuration, since apt-utils is not installed
#invoke-rc.d: policy-rc.d denied execution of start.
#invoke-rc.d: policy-rc.d denied execution of start.




def deploy():
    with cd('/etc/init'):
        env.warn_only = True
        run('service nginx restart')
