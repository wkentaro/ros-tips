Usage of sqlite3 & Python
=========================

Installation
++++++++++++
Install sqlite3 from command line::

  $ brew install sqlite3 # sqlite command on Mac OS X
  $ pip install sqlite3  # Python package


Get data from command line
++++++++++++++++++++++++++

sqlite3 interpreter from command line::

   $ sqlite3 database.sqlite3
   sqlite> CREATE TABLE tbl1 (id PRIMARY KEY NOT NULL, name DEFAULT '', email NOT NULL, password NOT NULL);
   sqlite> INSERT INTO tbl1 (name, email, password) VALUES ('Kentaro Wada', 'www.kentaro.wada@gmail.com', 'password');
   sqlite> SELECT name FROM tbl1 WHERE name = 'Kentaro Wada' AND email = 'www.kentaro.wada@gmail.com';
   sqlite> UPDATE name SET name = 'wkentaro' WHERE id = 1;


Manage SQLite3 with Python
++++++++++++++++++++

Connect database::

   >>> import sqlite3
   >>> conn = sqlite3.connect('database.sqlite3')
   >>> c = conn.cursor()

Get data from database::

   >>> sql = 'SELECT * FROM tbl1'
   >>> c.execute(sql)
   >>> data = c.fetchall()

Store data to database::

   >>> sql = """INSERT INTO tbl1 (name, email, password) VALUES ('Kentaro Wada', 'www.kentaro.wada@gmail.com', 'password')"""
   >>> c.execute(sql)
   >>> conn.commit()

Deconnect database::
  
   >>> conn.close()