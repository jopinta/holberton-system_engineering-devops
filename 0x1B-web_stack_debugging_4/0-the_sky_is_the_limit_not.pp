# under pressure and it turns out it’s not doing well
exec { 'Puppet-manifest'
  command  => 'sed -i s/15/4096/ /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}