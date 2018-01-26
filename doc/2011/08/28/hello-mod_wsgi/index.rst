Hello mod_wsgi
==============

.. post:: 2011/08/28
    :category: Buildout, Plone

**It seems I've inadvertently started another series of blog entry**

It seems I've inadvertently started another series of blog entry: the "hello world" series, wherein I explain how to easily get started with `various exciting Python technologies`_.

This time, in order to familiarize myself with `mod\_wsgi`_, I've created a buildout to automate some of the processes explained in:

- `http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide`_

(This series also helps me to subtly introduce the zc.buildout "extendables" I have been working on. More on those in a future post.)

The extendables
--------------------------------------------------------------------------------

The extendables make it easy to bootstrap a development environment with complex software requirements, via `zc.buildout`_. In this case, I want to be able to type:

::

    $ test-apache test-dir

And get a working, *disposable* Apache instance minutes later. I also want that Apache to come with a mod\_wsgi app installed and working.

Setup
--------------------------------------------------------------------------------

First we use the `aforementioned extendable`_, like so:

::

    $ virtualenv test-dir
    $ cd test-dir
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit the buildout.cfg to look like this:

::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x 

Run buildout:

::

    $ bin/buildout

Assuming successful completion, you should be able to run Apache in the foreground via:

::

    $ bin/supervisord -e debug -n

Now check http://localhost:8080.

This works because the `"extendable" (buildout configuration file)`_ contains:

-  The `little WSGI app`_ from the QuickInstallationGuide, templatized via `collective.recipe.template`_.
-  A `templatized httpd.conf file`_.

I like to automate the process even further with the `following script`_:

::

    #!/bin/shmkdir $1
    virtualenv-2.6 $1
    cd $1
    bin/easy_install zc.buildout
    bin/buildout init
    cat << EOF > buildout.cfg
    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x
    EOF
    bin/buildout
    bin/supervisord -e debug -n

Thus closing the loop on this blog entry, and making the following possible:

::

    $ test-apache test-dir

I've been using my `test-plone`_ script for years now, and I'm hoping that the test-apache script proves just as useful (especially as Plone moves closer to a WSGI-supporting stack via `Zope 2.13`_).

.. _various exciting Python technologies: http://blog.aclark.net/2011/08/20/hello-plone/
.. _mod\_wsgi: http://code.google.com/p/modwsgi/
.. _`http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide`: http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide
.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout/1.5.2
.. _aforementioned extendable: https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x
.. _"extendable" (buildout configuration file): https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x
.. _little WSGI app: https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/conf/app.wsgi.in
.. _collective.recipe.template: http://pypi.python.org/pypi/collective.recipe.template/1.9
.. _templatized httpd.conf file: https://github.com/ACLARKNET/build/blob/master/apache/2.2.x/httpd.conf.in
.. _following script: https://github.com/ACLARKNET/binfiles/blob/master/test-apache
.. _test-plone: https://github.com/ACLARKNET/binfiles/blob/master/test-plone
.. _Zope 2.13: http://pypi.python.org/pypi/Zope2/2.13.9
