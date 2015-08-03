What I do when cleanly installing Raspbian on Raspberry Pi.
===========================================================

Find RasPi IP
+++++++++++++
Find ip address of raspberry pi by scanning local network by
`IP Scanner <https://itunes.apple.com/us/app/ip-scanner/id404167149?mt=12>`_.
And login by ssh::

  $ ssh pi@[IP_ADDRESS]  # password is 'raspberry'


Basic config
++++++++++++

With :code:`sudo raspi-config`, change belows.

1. Expand Filesystem (expand filesystem size for ex. 3GB -> 30GB)
2. User Password (change password to login rapi and to be root)
3. Hostname (change hostname to find raspi ip in local network)
4. International Settings

   - Change Locale
   - Change Timezone

and install avahi-daemon for static hostname. ( for 3. )

.. code-block :: bash

  $ sudo apt-get install avahi-daemon


Airplay config
++++++++++++++

* http://www.raywenderlich.com/44918/raspberry-pi-airplay-tutorial


Printer config
++++++++++++++

Setup
-----

* Connect usb connector to Raspberry Pi, and check if it reacts by :code:`dmesg`.
* Install cups by :code:`sudo apt-get install cups`.
* Add user pi to cups. :code:`sudo usermod -a -G lpadmin pi`
* Edit config file. :code:`sudo vim /etc/cups/cupsd.conf`
    - :code:`Listern localhost:631` -> :code:`Listern 631`
    - Add :code:`Allow @local` after :code:`Order allow,deny`
* Restart cupsd. :code:`sudo /etc/init.d/cups restart`
* Add printer on :code:`http://[IP_ADDRESS]:631`.


Reference
---------
* http://furodrive.com/2014/05/pi_printer/

