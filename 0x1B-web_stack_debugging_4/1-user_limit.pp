# Fix high amount of files opened

exec {'rep':
  command => '/usr/bin/sudo /bin/sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
}
exec {'repl':
  command => '/usr/bin/sudo /bin/sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  require => Exec['rep']
}
