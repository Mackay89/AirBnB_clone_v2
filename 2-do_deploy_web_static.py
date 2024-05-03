#!/usr/bin/python3
"""
Fabric script that distributes an rchives to a ewb servers.
"""
import os 
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['54.158.80.63', '100.26.255.237']


def do_deploy(archive_path):
    """
    Distibutes an archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False


    try:
        put(archive_path, "/tmp/")


        archive_file = os.path.basename(archive_path)
        folder_name = '/data/web_static/releases/' + archive_file.split('.')[0]
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(archive_file, folder_name))
        run('rm /tmp/{}'.format(archive_file))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(folder_name))


        return True
    except Exception as e:
        print("Error deploying:", e)
        return False
