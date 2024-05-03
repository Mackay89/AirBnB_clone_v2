exec { 'sudo_apt-get_update':
  command => '/usr/bin/apt-get -y update',
}

exec { 'install_nginx':
  command => '/usr/bin/apt-get -y install nginx',
  require => Exec['sudo_apt-get_update'],
}

exec { 'create_test_directory':
  command => '/bin/mkdir -p /data/web_static/releases/test/',
}

exec { 'create_shared_directory':
  command => '/bin/mkdir -p /data/web_static/shared/',
}

file { '/data/web_static/releases/test/index.html':
  ensure => present,
  content => 'Puppet x School',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

exec { 'configure_nginx':
  command => '/bin/sed -i "/listen 80 default_sever/a location /hbnb_static/ {alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  require => Exec['install_nginx'],
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}

exec { 'set_permissions':
  command => '/bin/chown -R ubuntu:ubuntu /data',
}
