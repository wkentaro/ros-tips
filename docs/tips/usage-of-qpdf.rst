Usage of managing pdf password command qpdf
===========================================

Installation
++++++++++++
.. code-block:: bash

  $ brew install qpdf


Example
+++++++
.. code-block:: bash

  $ # Unlock pdf locked with password "test"
  $ qpdf --decrypt --password=test doc.locked.pdf doc.unlocked.pdf