# testing to install gem
exec { 'puppet-lint':
  command => '/bin/gem install puppet-lint'
}