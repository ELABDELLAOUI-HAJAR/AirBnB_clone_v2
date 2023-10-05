#!/usr/bin/python3
""" generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """ generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone repo
    """

    local("mkdir -p versions")
    dformat = "%Y%m%d%H%M%S"
    archive_path = "versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), dformat))
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path
