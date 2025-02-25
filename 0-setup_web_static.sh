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
FILE_DIRECTORY=/data/web_static/releases/test/
if ! [ -f "$FILE" ]; then
    mkdir -p "$FILE_DIRECTORY"
    printf "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > "$FILE"
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
IS_IN_FILE=$(grep -c "hbnb_static" $CONFIG_WEB)
if [ "$IS_IN_FILE" -eq 0 ];
then
   sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
   nginx -s reload
fi

#!/usr/bin/env bash
# Install Nginx
if ! [ -x "$(command -v nginx)" ]
then
   apt-get update -y
   apt-get install nginx -y
   service nginx start
fi
