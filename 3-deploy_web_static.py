#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers.
"""
import os
from fabric.api import env, run
from fabric.operations import put
from datetime import datetime
from os.path import isdir, exists


env.hosts = ['54.158.80.63', '100.26.255.237']


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir -p versions")
            file_name = "versions/web_static_{}.tgz".format(date)
            local("tar -cvzf {} web_static".format(file_name))
            return file_name
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Create and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

