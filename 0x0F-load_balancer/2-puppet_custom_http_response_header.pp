#automate the task of creating a custom HTTP header response, but with Puppet.
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['Nginx'],
}
exec {'Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => 'server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /usr/share/nginx/html;
	index index.html;
	add_header X-Served-By $HOSTNAME;
	location /redirect_me {
	  return 301 https://www.youtube.com;
	}
	error_page 404 /custom_404.html;
	location = /custom_404.html {
	  internal;
	}
      }',
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
