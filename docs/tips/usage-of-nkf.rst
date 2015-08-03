Usage of changing file encoding command nkf
===========================================

Installation
++++++++++++
.. code-block:: bash

  $ brew install nkf


Example
+++++++
.. code-block:: bash

  $ # Check string encoding
  $ nkf -g data1.sjis.csv
  Shift_JIS

  $ # Convert to UTF-8 (option: -w)
  $ nkf -w data1.sjis.csv > data1.utf8.csv
  $ nkf -g data1.utf8.csv
  UTF-8

  $ # Convert to Shift JIS (option: -s)
  $ # Convert with same filename (option: --overwrite)
  $ nkf -s --overwrite data1.csv
  $ nkf -g data1.csv
  Shift_JIS