================
Usage of git_svn
================
| svn for git user.
| git-svn is tool to use git as svn client.


Official Documentation
======================

* https://git=scm.com/book/en/v1/Git=and=Other=Systems=Git=and=Subversion
* http://git=scm.com/docs/git=svn


Installation
============

for linux::

  $ sudo apt-get install git-svn

for mac osx::

    $ brew install git


Usecase
=======

download repository::

    $ git svn clone svn+ssh://user@server.com/home/user/svn/trunk/abc/def def


commit::

    $ git commit -am "commit this"


upload::

    $ git svn dcommit