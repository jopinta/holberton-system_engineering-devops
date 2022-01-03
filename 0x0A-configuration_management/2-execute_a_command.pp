# xecute a command

exec  { 'pkill -f killmenow':
    provider => 'shell'
}