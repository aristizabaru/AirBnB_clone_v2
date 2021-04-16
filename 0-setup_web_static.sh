#!/usr/bin/env bash
# Install Nginx
if ! [ -x "$(command -v nginx)" ]
then
   apt-get update -y
   apt-get install nginx -y
   service nginx start
fi

# Create directories and index.html
if ! [ -f /data/web_static/releases/test/index.html ]; then
    mkdir -p /data/web_static/releases/test/
    echo -e  "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
fi

# Create directory shared
if ! [ -d /data/web_static/shared/ ]; then
    mkdir -p /data/web_static/shared/
fi

# Create soft link from current to test directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change owner
chown -R ubuntu:ubuntu /data/

# Change Nginx configuration file
IS_IN_FILE="$(grep -c hbnb_static /etc/nginx/sites-available/default)"
if [ "$IS_IN_FILE" -eq 0 ];
then
   sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t}" /etc/nginx/sites-available/default
   nginx -s reload
fi
