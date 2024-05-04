exec { 'sudo apt-get-update':
  command => '/usr/bin/apt-get -y update',
}

exec { 'b':
  command => '/usr/bin/apt-get -y install nginx',
  require => Exec['sudo apt-get-update']
}

exec { 'c':
  command => '/bin/mkdir -p /data/web_static/releases/test/',
}

exec { 'd':
  command => '/bin/mkdir -p /data/web_static/shared/',
}

exec { 'e':
  command => '/bin/echo "Puppet x School" > /data/web_static/releases/test/index.html',
}

exec { 'f':
  command => '/bin/ln -sf /data/web_static/releases/test /data/web_static/current',
}

exec { 'h':
  command => '/bin/sed -i "/listen 80 default_sever/a location /hbnb_static/ {alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

exec { 'i':
  command => '/usr/sbin/service nginx restart',
}

exec { 'g':
  command => '/bin/chown -R ubuntu:ubuntu /data',
}
