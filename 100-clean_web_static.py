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
    local("mkdir -p versions")
    file_name = "versions/web_static_{}.tgz".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
    return file_name

def do_deploy(archive_path):
    """
    Function to distribute an archive to a server
    """
    if not os.path.exists(archive_path):
        return False
    rex = r'^versions/(.+)\.tgz'
    match = re.search(rex, archive_path)
    if not match:
        print("Invalid archive path format.")
        return False
    file_name = match.group(1)
    res = put(archive_path, "/tmp/{}.tgz".format(file_name))
    if res.failed:
        print("Failed to upload archive to server.")
        return False
    try:
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(file_name, file_name))
        run("rm /tmp/{}.tgz".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* " "/data/web_static/releases/{}/".format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(file_name))
        print("New version deployed!")
        return True
    except Exception as e:
        print("Error deploying:", e)
        return False

def deploy():
    """
    Creates and distributes an archive to web server
    """
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        file = local("ls -1t versions", capture=True)
        file_names = file.split(" ")
        n = int(number)
        if n in (0, 1):
            n = 1
        for i in file_names[n:]:
            local("rm versions/{}".format(i))


        dir_server = run("ls -1t /data/web_static/releases")
        dir_server_names = dir_server.split(" ")
        for i in dir_server_names[n:]:
            if i != "test":
                run("rm -rf /data/web_static/releases/{}".format(i))
    except Exception as e:
        print("Error cleaning:", e)
