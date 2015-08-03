Apache config for WSGI with Python
==================================

Hosting
+++++++

Edit :code:`/etc/apache2/sites-available/jishupro.conf`::

  <VirtualHost *:80>
    ServerName keyopener.ddo.jp
    WSGIScriptAlias / /home/pi/Work/jishupro/website/jishupro.wsgi
  </VirtualHost>


Reflect the config with below.::

  $ sudo a2ensite jishupro.conf
  $ sudo apachectl restart