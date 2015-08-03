Apache with sudo
================

Change Apache authority
+++++++++++++++++++++++

Add below by :code:`sudo visudo`::

   # For raspberry pi
   www-data  ALL=(ALL) NOPASSWD: /usr/bin/python

   # Ubuntu
   apache  ALL=(ALL) NOPASSWD: /usr/bin/python