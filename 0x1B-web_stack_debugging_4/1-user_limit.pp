# Change the OS config
exec { 'holberton':
command => sed -i 's/holberton soft nofile 4/holberton soft nofile/g' etc/security/limits.conf sed -i
provider => shell,
}

exce {
command => sed -i 's/holberton hard no file 5/holberton hard no file/g' etc/security/limits.conf
privider => shell,
}