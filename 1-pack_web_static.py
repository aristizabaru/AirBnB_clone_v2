#!/usr/bin/python3
"""module 1-pack_web_static.py"""
from fabric.api import *
from datetime import datetime
from os.path import isdir, getsize


def do_pack():
    """pack static_web"""

    # config
    time_stamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(time_stamp)
    assets = "web_static"
    target_dir = "versions"

    print("Packing {} to {}/{}".format(assets, target_dir, file_name))

    # find if directory is valid
    if not isdir(target_dir):
        if local("mkdir {}".format(target_dir)).failed:
            return None

    # compress files
    if local("tar -cvzf {}/{} {}".format(target_dir, file_name,
                                         assets)).failed:
        return None

    # print status
    file_size = getsize("{}/{}".format(target_dir, file_name))
    print("{} packed: {}/{} -> {}Bytes".format(assets,
          target_dir, file_name, file_size))

    return "{}/{}".format(target_dir, file_name)
