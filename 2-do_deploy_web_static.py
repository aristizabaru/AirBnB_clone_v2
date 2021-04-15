#!/usr/bin/python3
"""2-do_deploy_web_static.py"""
from fabric.api import *
from datetime import datetime
from os.path import isdir, getsize, isfile

servers_list = {
    "2210-web-01": "34.75.110.34",
    "2210-web-02": "35.229.72.142"
}

env.roledefs = {
    'servers': [servers_list['2210-web-01'], servers_list['2210-web-02']]
}


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

# add decorator to only execute servers


@roles('servers')
def do_deploy(archive_path):
    """deploy static"""

    # config
    if isfile(archive_path) is False:
        return False
    file_name = archive_path.split("/")[1]
    # put(local, remote)
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p /data/web_static/releases/{}".format(file_name[:-4]))
        run("tar -xzf /tmp/{} -C "
            "/data/web_static/releases/{}/".format(file_name,
                                                   file_name[:-4]))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                file_name[:-4], file_name[:-4]))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            file_name[:-4]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(
                file_name[:-4]))
        print("New version deployed!")
        return True
    except Exception:
        return False
