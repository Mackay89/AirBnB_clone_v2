#!/usr/bin/python3
"""
Fabric script based on the file 3-deploy_web_static.py) that deletes out-of-date archives.
"""
import os
from fabric.api import env,run, local
from datetime import datetime
from os.path import exists, isfile
import re


env.hosts = ['54.158.80.63', '100.26.255.237']


def do_pack():
    """
    Function to compress files in an archive
    """
    local("mkdir -p varsions")
    file_name = "versions/web_static_{}.tgz".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
    return file_name

def do_deploy(archive_path):
    """
    Function to distribute an archive to a server
    """
    if not os.pathexists(archive_path):
        return False
    rex = r'^versions/(.+)\.tgz'
    match = re.search(rex, archive_path)
    if not match:
        print('Invalid archive path format.")
        return False
