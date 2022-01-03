# testing to install gem
exec { 'puppet-lint -v 2.5.0':
  ensure   => '1.1.0',
  provider => 'gem',
}