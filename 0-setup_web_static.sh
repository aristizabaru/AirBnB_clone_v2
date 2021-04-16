#!/usr/bin/env bash
# Install Nginx
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t}" /etc/nginx/sites-available/default
service nginx restart
