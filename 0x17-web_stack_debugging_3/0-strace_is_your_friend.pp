# use whatever Puppet resource
exec {
command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}