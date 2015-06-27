==================================
SSH Forwarding and ssh_cofig file
==================================

Port Forwarding
---------------
Enable port forwarding by::

  $ ssh -L 9901:private-computer.com:22 user@staging-computer.com

After this, you can access your ``private-computer.com`` by::

  $ ssh user@localhost -p 9901


Write ssh_config for Port Forwarding
------------------------------------
Write below::

  Host tunnel
    HostName staging-computer.com
    LocalForward 9901 private-computer.com:22
    User user

And enable port forwarding::

  $ ssh -f -N tunnel

After this you can also do::

  $ ssh user@localhost -p 9901