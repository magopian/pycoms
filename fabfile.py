#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run, cd, env, roles


env.roledefs = {
    'prod': ['agopian@ad'],
}


# do not execute .profile and .bashrc when opening a ssh session
# this will avoid the "err: stdin: is not a tty?" message
env.shell = '/bin/bash -c'


@roles('prod')
def deploy():
    """Deploys on the prod server"""
    with cd('~/www/pycoms/'):
        run('git pull')
        run('venv/pelican -s settings.py -t theme/ content/')
