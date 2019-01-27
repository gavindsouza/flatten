flatten
==================================================
*"Image Compression using Digital Signal Processing"*

..
|Build Status| |Documentation Status|

.. |Build Status| image:: https://travis-ci.org/gavindsouza/flatten.svg?branch=master
   :target: https://travis-ci.org/gavindsouza/flatten

.. |Documentation Status| image:: https://readthedocs.org/projects/flatten/badge/?version=latest
   :target: http://flatten.readthedocs.io/en/latest/?badge=latest


Table of Contents
~~~~~~~~~~~~~~~~~

-  `Installation`_
-  `Usage`_
-  `Dependencies`_
-  `Sample Images`_
-  `License`_


Installation
~~~~~~~~~~~~

Clone the git repository:


.. code:: console

   $ git clone https://github.com/gavindsouza/flatten.git
   $ cd flatten

Install necessary dependencies


.. code:: console

   $ pip install -r requirements.txt

Go ahead and install as follows:


.. code:: console

   $ python setup.py install


Usage
~~~~~
If package is installed, go ahead and type the following in the console else just change to module directory

.. code:: console

   $ python -m flatten --src IMAGE_PATH

this will create a compressed form of the image in the same folder


Dependencies
~~~~~~~~~~~~~

- numpy
- matplotlib

.. _Dependencies: requirements.txt

Sample Images
~~~~~~~~~~~~~~

The very large Sample Images obtained from `effigis Geo Solutions`_

.. _effigis Geo Solutions: https://www.effigis.com/en/solutions/satellite-images/satellite-image-samples/

License
~~~~~~~

This code has been released under the `MIT License`_.

.. _MIT License: LICENSE