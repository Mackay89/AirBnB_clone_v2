#!/usr/bin/env bash
# Script that sets up a web server for deployment of web_static.


apt-get update
apt-get install -y nginx


sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello World" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current


owner=$(stat -c "%U" /)
group=$(stat -c "%G" /)
chown -R "$owner" /data/
chgrp -R "$group" /data/


cat >/etc/nginx/sites-available/default <<EOF
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root  /var/www/html;
	index  index.html index.html;


	location /hbnb_static {
        	alias /data/web_static/current/;
	     	try_files $uri $uri/ =404;
	}

	location /redirect_me {
		return 301 http://mack4y.tech/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}
EOF

service nginx restart
