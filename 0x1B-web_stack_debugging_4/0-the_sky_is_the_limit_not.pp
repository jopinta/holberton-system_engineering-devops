# under pressure and it turns out it’s not doing well

exec {
  provider => shell,
  command => 'sed -i s/15/4069/ /etc/default/nginx',
  notify => Service['nginx'],
}