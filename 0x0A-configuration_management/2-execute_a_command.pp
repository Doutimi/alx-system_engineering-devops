# a manifest that kills a process named killmenow

exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
  onlyif  => 'pgrep killmenow',
}
