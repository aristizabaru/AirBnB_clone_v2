#!/usr/bin/env bash
# Install Nginx
if ! [ -x "$(command -v nginx)" ]
then
   apt-get update -y
   apt-get install nginx -y
   service nginx start
fi

# create files

mkdir -p /data/web_static/releases/test/
echo -e  "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html

# Create directory shared
mkdir -p /data/web_static/shared/

# Create soft link from current to test directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change owner
sudo chown -R ubuntu:ubuntu /data/

# Change Nginx configuration file
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t}" /etc/nginx/sites-available/default
sudo service nginx reload


