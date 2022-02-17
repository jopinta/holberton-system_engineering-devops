# use whatever Puppet resource
exec { 'strace_is_your_friend':
command => "sed -i s/phpp/php/g /var/www/html/wp-settings.php",
path => '/bin';
}