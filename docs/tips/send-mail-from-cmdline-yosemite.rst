Send mails from command line on Mac OS X 10.10 Yosemite
=======================================================

Edit mail.cf
++++++++++++
Add following line on /etc/postfix/main.cf. :code:`$ sudo vim /etc/postfix/main.cf`


.. code-block :: pfmain

   relayhost = [smtp.gmail.com]:587
   smtp_sasl_auth_enable = yes
   smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
   smtp_sasl_security_options = noanonymous
   smtp_use_tls = yes
   smtp_sasl_mechanism_filter = plain # only for yosemite


Add password config file
++++++++++++++++++++++++
Add following line on /etc/postfix/sasl_passwd. :code:`$ sudo vim /etc/postfix/sasl_passwd`

.. code-block :: pfmain

   [smtp.gmail.com]:587 username@gmail.com:password


Reflect config change
+++++++++++++++++++++
Run the following commands.

.. code-block :: bash

   $ sudo chmod 600 /etc/postfix/sasl_passwd
   $ sudo postmap /etc/postfix/sasl_passwd
   $ sudo launchctl stop org.postfix.master
   $ sudo launchctl start org.postfix.master


Test
++++

.. code-block :: bash

   $ date | mail -s "testing" email@adderess.to


Reference
+++++++++
* http://owleon.blogspot.jp/2014/11/command-line-mail-with-gmail-smtp-on.html