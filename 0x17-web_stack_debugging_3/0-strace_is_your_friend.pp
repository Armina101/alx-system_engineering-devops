# Replacing a line in a file on the server

$file_to_edit = '/var/www/html/wp-settings.php'

#replace the line with  "phpp" to "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
