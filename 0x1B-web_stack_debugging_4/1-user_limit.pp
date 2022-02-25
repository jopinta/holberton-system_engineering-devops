# Change the OS config
exec {
command => s/holberton soft nofile 4/holberton soft nofile/g etc/security/limits.conf sed -i
provider => shell,
}

exce {
command => s/holberton hard no file 5/holberton hard no file/g etc/security/limits.conf sed -i
privider => shell,
}