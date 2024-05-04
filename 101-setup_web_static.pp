exec { 'sudo apt-get-update':
  command => '/usr/bin/apt-get -y update',
}

exec { 'b':
  command => '/usr/bin/apt-get -y install nginx',
  require => Exec['sudo apt-get-update']
}

exec { 'c':
  command => '/bin/mkdir -p /data/web_static/releases/test/',
  path    => '/bin',
}

exec { 'd':
  command => '/bin/mkdir -p /data/web_static/shared/',
  path    => '/bin',
}

exec { 'e':
  command => '/bin/echo "Puppet x Holberton School" > /data/web_static/releases/test/index.html',
  path    => '/bin',
}

exec { 'f':
  command => '/bin/ln -sf /data/web_static/releases/test /data/web_static/current',
  path    => '/bin',
}

exec { 'h':
  command => '/bin/sed -i "/listen 80 default_sever/a location /hbnb_static/ {alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  path    => '/bin'
}

exec { 'i':
  command => '/usr/sbin/service nginx restart',
}

exec { 'g':
  command => '/bin/chown -R ubuntu:ubuntu /data',
  path    => '/bin'
}
