# manifest for installing and writing custom directives for nginx
# it has to be in order, more to avoid confusion

# installs nginx
package { 'nginx':
  ensure => 'installed',
}

# creates an hello world html file in the www/html folder
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# creates an 404 html file in the www/html folder
file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page.",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# write custom directive for redirection and 404 page
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location / {
      try_files \$uri \$uri/ =404;
}

    location /redirect_me {
      return 301 https://www.github.com/meistens/;
}

    error_page 404 /404.html;
    location = /404.html {
      internal;
      root /var/www/html;
}
",
}

# change file site where nginx should host
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# restart nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
