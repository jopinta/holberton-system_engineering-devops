# under pressure and it turns out it’s not doing well
exec {
  command  => 'sed -i s/15/4069/ /etc/default/nginx',
  provider => shell,
  notify   => Service['nginx'],   
}