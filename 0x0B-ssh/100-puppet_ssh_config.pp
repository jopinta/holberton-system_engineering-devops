#Let’s practice using Puppet to make changes to our configuration file.

file_line {'Turn off passwd auth':
   path => '/etc/ssh/ssh_config'
   line => 'PasswordAuthentication no' 
}