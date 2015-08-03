Usage of scikit-learn
=====================

Installation
++++++++++++
.. code-block :: bash

   $ pip install scikit-learn


Get data
++++++++

sklearn.datasets.fetch_mldata
-----------------------------
Get dataset from mldata.org.

.. code-block :: python

   from sklearn.datasets import fetch_mldata
   # argument of fetch_mldata is found in http://mldata.org/

   # MNIST
   mnist = fetch_mldata('MNIST original')
   X = mnist.data
   y = mnist.target

   # Digits
   digits = fetch_mldata('digits')
   X = digits.data
   y = digits.target


sklearn.cross_validation.StratifiedKFold
----------------------------------------
Cross validation using sklearn.cross_validation.StratifiedKFold.

.. code-block :: python

  scores = np.zeros(len(skf))
  skf = StratifiedKFold(y, n_folds=3)
  for i, (train_index, test_index) in enumerate(skf):
      clf.fit(X[train_index], y[train_index])
      score = clf.score(X[test_index], y[test_index])
      scores[i] = score


Reference
+++++++++
* http://scikit-learn.org/stable/index.html