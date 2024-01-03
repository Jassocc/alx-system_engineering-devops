#nginx with puppet
package { 'nginx':
  ensure => installed,
}
file { '/usr/share/nginx/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => @(EOT)
	server {
		listen 80 default_server;
		listen [::]:80 default_server;

		root /usr/share/nginx/html;
		index index.html;

		location /redirect_me {
			return 301 https://youtube.com;
		}

		location / {
			return 200 "Hello World!";
		}
  }
  EOT
  require => Package['nginx'],
  notify  => Service['nginx'],
}
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
