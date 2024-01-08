#automate the task of creating a custom HTTP header response, but with Puppet.
exec { 'update':
  provider => shell,
  command  => 'apt-get -y update',
}
exec { 'install':
  provider => shell,
  command  => 'apt-get -y install nginx',
}
exec { 'config':
  provider => shell,
  command  => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
}
exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
