#!/usr/bin/env python
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from fabric.api import *
from toughradius import __version__

env.user = 'root'
env.hosts = ['128.199.107.135']

def pypi():
    with cd("/opt/toughradius"):
        run('git pull origin stable')
        run('make upload')

def tag():
    local("git tag -a v%s -m 'version %s'"%(__version__,__version__))
    local("git push all v%s:v%s"%(__version__,__version__))