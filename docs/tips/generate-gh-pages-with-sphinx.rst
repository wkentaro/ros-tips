Generate GitHub Pages with Sphinx
=================================

Generate gh-pages
+++++++++++++++++
First, you should generate gh-pages branch and GitHub pages. ::

  cd repo
  git checkout --orphan gh-pages
  git rm -rf .
  echo "First commit" > index.html
  git add .
  git commit -m "Just to create the branch."
  git push origin gh-pages

Run sphinx-quickstart
+++++++++++++++++++++
Generate sphinx base files. ::

  git checkout master
  sphinx-quickstart # in second option you should say yes

Add build target
++++++++++++++++
Add below in Makefile. ::

  GH_PAGES_SOURCES = source code wiki Makefile

  ...

  gh-pages:
      git checkout gh-pages
      rm -rf build _sources _static
      git checkout master $(GH_PAGES_SOURCES)
      git reset HEAD
      make html
      mv -fv build/html/* ./
      rm -rf $(GH_PAGES_SOURCES) build
      git add -A
      git ci -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master


Add documents
+++++++++++++
If you add new documents, you can build and publish it by running below.::

  vim source/expert_python.rst
  make gh-pages

Reference
+++++++++
* http://blog.nikhilism.com/2012/08/automatic-github-pages-generation-from.html