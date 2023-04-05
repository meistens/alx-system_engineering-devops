# Manifest installs the package flask via pip3

# installs pip3 if not installed
package { 'python3-pip':
  ensure => installed
}

# installs flask
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
