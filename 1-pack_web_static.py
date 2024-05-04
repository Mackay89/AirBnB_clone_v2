#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static
# folder of your AirBnB Clone repo, using the function do_pack.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.
    """
    try:
        dt = datetime.utcnow()
        file_name = "versions/web_static_{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(e)
        return None
