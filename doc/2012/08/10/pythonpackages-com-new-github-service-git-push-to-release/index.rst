Pythonpackages.com: New GitHub Service - Push to Release
========================================================

.. post:: 2012/08/10
    :category: Python

**pythonpackages.com helps Python programmers package and release their software with just a few clicks.**

PythonPackages GitHub Service
--------------------------------------------------------------------------------

There is a new `GitHub Service`_ available for pythonpackages.com that allows you to release Python packages from GitHub to the Python Package Index, simply by pushing a commit message that begins with "Release" e.g.:

::

    $ git commit -a -m "Release 1.0"; git push

(The release creates a tag with the appropriate version number, extracted from setup.py) To use the service, please follow the instructions below.

Instructions
------------

-  Sign up for the pythonpackages.com beta: `http://pythonpackages.com/signup`_.
-  Follow the `Introduction`_ instructions.
-  On the Python Package Index, authorize pythonpackages.com to act on your behalf, as explained here: http://blog.aclark.net/pythonpackagescom-using-pypi039s-oauth1-support-to-register-and-upload-packages.html (**pythonpackages.com -> Dashboard -> Manage accounts -> PyPI -> Authorize**).
-  On GitHub, configure the PythonPackages service to be Active on any repository that contains a Python package you want to release (**Repo -> Admin -> Service Hooks -> PythonPackages -> [\*] Active**).

Now you can git push to release! If you have any trouble, please `open a ticket`_. These instructions will live permanently here: http://docs.pythonpackages.com/en/latest/github-service.html.

.. _GitHub Service: https://github.com/github/github-services
.. _`http://pythonpackages.com/signup`: http://pythonpackages.com/signup
.. _Introduction: http://docs.pythonpackages.com/en/latest/introduction.html
.. _`http://blog.aclark.net/2012/08/07/pythonpackages-com-using-pypis-oauth1-support-to-register-and-upload-packages`: http://blog.aclark.net/2012/08/07/pythonpackages-com-using-pypis-oauth1-support-to-register-and-upload-packages
.. _open a ticket: https://bitbucket.org/pythonpackages/pythonpackages.com/issues/new
.. _`http://docs.pythonpackages.com/en/latest/github-service.html`: http://docs.pythonpackages.com/en/latest/github-service.html
