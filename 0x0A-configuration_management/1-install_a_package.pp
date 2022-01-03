# testing to install
package { 'puppet-lint':
  ensure          => '1.1.0',
  provider        => 'gem',
  install_options => '-v 2.5.0',
}