#!/usr/bin/env bash
# Install Nginx
if ! [ -x "$(command -v nginx)" ]
then
   sudo apt-get update -y
   sudo apt-get install nginx -y
   sudo service nginx start
fi

# Create directories and index.html
FILE=/data/web_static/releases/test/index.html
DATA="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
FILE_DIRECTORY=/data/web_static/releases/test/
if [ -f "$FILE" ]; then
    mkdir -p "$FILE_DIRECTORY"
    echo -e  "$DATA" > "$FILE"
fi

# Create directory shared
DIRECTORY=/data/web_static/shared/
if ! [ -d "$DIRECTORY" ]; then
    mkdir -p "$DIRECTORY"
fi

# Create soft link from current to test directory
LINK=/data/web_static/current
TARGET=/data/web_static/releases/test/
ln -sf "$TARGET" "$LINK"

# Change owner
chown -R ubuntu:ubuntu /data/

# Change Nginx configuration file
CONFIG_WEB=/etc/nginx/sites-available/default
DATA="\\\n\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t}"
IS_IN_FILE=$(grep -c "hbnb_static" $CONFIG_WEB)
if [ "$IS_IN_FILE" -eq 0 ];
then
   sed -i "/server_name _;/ a $DATA" "$CONFIG_WEB"
   nginx -s reload
fi

#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static
# apt-get update
# mkdir -p /data/
# mkdir -p /data/web_static/
# mkdir -p /data/web_static/releases/
# mkdir -p /data/web_static/shared/
# mkdir -p /data/web_static/releases/test/
# echo " <h1 align=\"center\"> Cool You Nginx configuration is ready 🦾</h1> " > /data/web_static/releases/test/index.html
# ln -s -f /data/web_static/releases/test/ /data/web_static/current
# chown -R ubuntu:ubuntu /data/
# # Install Nginx in my server
# apt-get -y install nginx
# # config hbnb_static as alias
# sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
# # restarts the server
# service nginx restart
