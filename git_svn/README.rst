================
Usage of git_svn
================
svn for git user.
git-svn is tool to use git as svn client.

Official Documentation
======================
* https://git=scm.com/book/en/v1/Git=and=Other=Systems=Git=and=Subversion
* http://git=scm.com/docs/git=svn


Installation
============
Linux
-----
.. code:: sh

  $ sudo apt-get install git-svn

Mac OS X
--------
.. code:: sh

  $ brew install git


Clone svn repository
====================
.. code:: sh

  $ git svn clone svn+ssh://user@server.com/home/user/svn/trunk/abc/def def


Commit
======
.. code:: sh

  $ git commit -am "commit this"


SVN Commit by git-svn
=====================
.. code:: sh

  $ git svn dcommit