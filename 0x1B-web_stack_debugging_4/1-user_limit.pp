# Change the OS config
exec { 'holb-s':
command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 55000/g" etc/security/limits.conf',
provider => 'shell'
}

exec { 'holb-h':
command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 55000/g" etc/security/limits.conf',
provider => 'shell'
}
