# use whatever Puppet resource
exec {
command => "sed -i s/phpp/php/g /var/www/html/wp-settings.php,
provider => '/bin'
}