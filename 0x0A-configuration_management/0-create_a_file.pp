# Create a file using Puppet

file { '/tmp/school':
  mode    => '0744',
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  path    => '/tmp/school',
  content => 'I love Puppet',
}
