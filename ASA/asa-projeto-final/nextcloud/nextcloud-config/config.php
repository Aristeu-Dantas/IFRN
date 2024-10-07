<?php
$CONFIG = array (
  'htaccess.RewriteBase' => '/',
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'apps_paths' =>
  array (
    0 =>
    array (
      'path' => '/var/www/html/apps',
      'url' => '/apps',
      'writable' => false,
    ),
    1 =>
    array (
      'path' => '/var/www/html/custom_apps',
      'url' => '/custom_apps',
      'writable' => true,
    ),
  ),
  'upgrade.disable-web' => true,
  'instanceid' => 'ocu42rj8ajr9',
  'passwordsalt' => 'ei6znmK43utPYG2JB7br6VcD0a5Ub1',
  'secret' => 'eMgFJyfHzEUR0Is35RIrsHkU1U3bpSgbmp1um25rNJFDDDmp',
  'trusted_domains' =>
  array (
    0 => 'localhost:8080',
    2 => 'nextcloud.ifrn.asa.br',
  ),
  'datadirectory' => '/var/www/html/data',
  'dbtype' => 'mysql',
  'version' => '29.0.6.1',
  'overwrite.cli.url' => 'http://localhost:8080',
  'dbname' => 'nextcloud',
  'dbhost' => 'db3',
  'dbport' => '',
  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'nextcloud',
  'dbpassword' => 'admin',
  'installed' => true,
  'app.mail.verify-tls-peer' => false,
  'mail_smtpdebug' => true,
  'loglevel' => 2,
  'debud' => true,
  'mail_smtpmode' => 'smtp',
  'mail_sendmailmode' => 'smtp',
  'mail_from_address' => 'teste',
  'mail_domain' => 'ifrn.asa.br',
  'mail_smtphost' => 'postfix',
  'mail_smtpport' => '25',
  'mail_smtpstreamoptions' =>
  array (
    'ssl' =>
    array (
      'allow_self_signed' => true,
      'verify_peer' => false,
      'verify_peer_name' => false,
    ),
  ),
  'defaultapp' => '',
);
