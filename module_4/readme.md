# Name: Mehdi (MED) Shakeri(mshakeri4@jh.edu)

# Module Info: Module 4 - Pytest and Sphinx, due 06/30/2024 at 11:59pm 


In this assignment we write scalable unit tests using pytest and make application’s documentation more easily available (and stylized) using sphinx.  We will construct extensible pizza ordering application: a service that allows other developers to quickly build upon our restaurant template and extend to new menu items and processes.

----------------------------------

In order.py we create an order object that initalizes list of pizzas = [].  This is a list
since order can be for several pizzas.  The list is initially set to none and total
aggregate order cost is 0.00.

Input the customers order for a given pizza goes into input_pizza() method.
In it we initialize the pizza object and attach to the order list of pizzas[].  We also
update the cost.

Pizza object simply sets cost to 0.00 and creates the pizza using the given parameters.

---------------------
# Approach explaining how to create Sphinx documentation and how to connect to RTD: 

After creating the Order pizza project, document using following approach:

-We create a folder called docs in the root folder

-We must run sphinx-quickstart in root folder of the project :

C:\Module 4 - Pytest and Sphinx\docs>sphinx-quickstart

The above command asks name of the project and a few other question. Answer N to separate builds and source.  This will create several folders and files:

_builds
_static
_templates
config.py
index.rst
make.bat
Makefile

We go into config.py and add followings:

import os, sys
sys.path.insert(0, os.path.abspath(".."))

Also add to config.py:

extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme"]

Then go to root level and run :

C:\Module 4 - Pytest and Sphinx>sphinx-apidoc -o docs src/

Above should create some more files in the docs folder.

Connect to github and push the files to SphinxPizzaOrder repository.  Then go to RTD
and build the document project.

To see SphinxPizzaOrder documents online please visit following link:

https://sphinxpizzaorder.readthedocs.io/en/latest/index.html#

Known Bugs:

What bugs?
