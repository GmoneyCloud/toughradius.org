#!/usr/bin/env python
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from fabric.api import *
from toughradius import __version__

env.user = 'root'
env.hosts = ['121.40.178.134']


def deploy():
    with cd("/var/www/toughradius.org"):
        run('git pull origin master')
        run('service nginx reload')



    