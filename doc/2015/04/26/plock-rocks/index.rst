Plock Rocks
===========

.. post:: 2015/04/26
    :category: Buildout, Plone

**Pip installs Plock. Plock installs Plone.**

.. image:: /images/plock-meme.png
    :alt: Plock Meme
    :align: center
    :class: img-thumbnail

Understanding Plock
-------------------

To understand Plock, you must understand:

- The undisputed complexity of the Plone stack [1]_.
- My desire to simplify, clarify and reduce-to-bare-elements everything I touch.
- My willingness to mask complexity when eliminating it is not possible, despite the risk of contributing to it.

Pyramid author Chris McDonough [2]_ once made a comment a long time ago to the effect: "Let's stop piling more crap on top of Plone" and that sentiment still resonates today. That's why even though I love small and useful tools like Plock, it pains me to know what Plock is doing "under the hood" [7]_. Nevertheless, I felt compelled to write it because not having it is worse.

Before I tell you what Plock is [8]_, let me briefly describe what Plone is.

What is Plone, really?
----------------------

What is the complexity I mention above? Briefly, with as few loaded statements as possible:

- **Zope2** "application server". This is something you can ``pip install`` but the results will not be usable [3]_.

- **Zope2 add-ons** AKA "products", most notably the Zope2 Content Management Framework (CMF). This is something you install on top of Zope2 (conceptually but not literally, ``pip install Products.CMFCore``) that provides typical content management features e.g. personalization, workflow, cataloging, etc.

- **Zope3** technologies e.g. the Zope Component Architecture (ZCA). These are things that are included-or-integrated with Zope2 and Plone. [4]_

- **Buildout** technologies e.g. setuptools, console scripts, recipes, extensions, etc. You can't easily build Plone without them, so we may as well declare them as dependencies.

- **Plone** technologies. Plone was originally known as a "skin for CMF" but has become much more than that.

    - **Archetypes** Legacy content type framework.

    - **Dexterity** Modern content type framework based on modern Zope concepts e.g. "Reuse over reinvention".

    - **Diazo** Modern theming engine based on XSLT that "maps Plone content to generic website themes."

In total, if you ``pip install Plone`` over 200 Python packages are installed [5]_.

What is Plock, really? 
----------------------

OK now it's time to explain Plock. Plock is something:

- you **install from PyPI** via ``pip install plock``. "Pip installs packages. Plock installs Plone."
- you use to **install Plone** without having to know about tarballs or Buildout.
- you use to **install Plone add-ons** without having to know about Buildout.

In one sentence: Plock runs Buildout so you don't have to, at least initially.

First steps with Plock
----------------------

Step #1
~~~~~~~

The first step with Plock [9]_ is that light bulb moment when you say to yourself: "I've heard that Plone is the ultimate open source enterprise CMS and I'd love to try it!" But you aren't willing to download a compressed archive and run the installer nor are you willing to ``pip install zc.buildout`` and figure the rest out for yourself. Enter Plock.

Step #2
~~~~~~~

The second step with Plock is knowing that it exists you can install it with: ``pip install plock``.

Step #3
~~~~~~~

The third step with Plock is using it to install Plone::

    $ plock plone
    Creating virtualenv... (plone)
    Installing buildout...
    Downloading installer (https://launchpad.net/plone/4.3/4.3.4/+download/Plone-4.3.4-r1-UnifiedInstaller.tgz)
    Unpacking installer...
    Unpacking cache...
    Installing eggs...
    Installing cmmi & dist...
    Configuring cache...
    Running buildout...
    Done, now run:
      plone/bin/plone fg

Now Plock's work is done; visit the following URL: http:://localhost:8080 and you should see:

.. image:: /images/plock-screen-1.png
    :alt: Plock Screen 1
    :align: center
    :class: img-thumbnail

Create a Plone site:

.. image:: /images/plock-screen-2.png
    :alt: Plock Screen 2
    :align: center
    :class: img-thumbnail

Start using Plone:

.. image:: /images/plock-screen-3.png
    :alt: Plock Screen 3
    :align: center
    :class: img-thumbnail

Next steps with Plock
---------------------

Plock is more than just a way to install the latest stable version of Plone quickly and easily. It's also a way to find and install Plone add-ons quickly and easily, and a way to install almost any version of Plone including the upcoming Plone 5 release.

Installing Add-ons
~~~~~~~~~~~~~~~~~~

Step #1
+++++++

List all Plone-related packages on PyPI:: 

    $ plock -l
    1) 73.unlockItems                           - A small tool for unlocking web_dav locked item in a plone portal.
    2) actionbar.panel                          - Provides a (old) facebook style action panel at the bottom of your  Plone site
    3) adi.init                                 - Deletes Plone's default contents        
    4) adi.samplecontent                        - Deletes Plone's default content and adds some sample content
    5) adi.slickstyle                           - A slick style for Plone portals, easily extendable for your own styles.
    6) affinitic.simplecookiecuttr              - Basic integration of jquery.cookiecuttr.js for Plone 3
    7) anthill.querytool                        - GUI for AdvancedQuery with some extensions - searching the easy way for Plone
    8) anthill.skinner                          - Skinning for plone made easy            
    9) anz.dashboard                            - Plone netvibes like dashboard implementation
    10) anz.ijabbar                              - Integrate iJab(an open source XMPP web chat client recommended by xmpp.org) to your plone site.
    …
    1,352) zopeskel.diazotheme                      - Paster templates for Plone Diazo theme package
    1,353) zopeskel.niteoweb                        - Paster templates for standard NiteoWeb Plone projects
    1,354) zopyx.ecardsng                           - An ECard implementation for Plone       
    1,355) zopyx.existdb                            - Plone-ExistDB integration               
    1,356) zopyx.ipsumplone                         - Lorem ipsum text and image demo content for Plone
    1,357) zopyx.multieventcalendar                 - A multi-event calendar for Plone 3.X    
    1,358) zopyx.plone.cassandra                    - Show all assigned local roles within a subtree for any Plone 4 site
    1,359) zopyx.plone.migration                    - Export/import scripts for migration Plone 2+3 to Plone 4
    1,360) zopyx.smartprintng.plone                 - Produce & Publisher server integration with Plone
    1,361) zopyx.together                           - Plone integration with together.js      

Step #2
+++++++

.. note::

    Plock currently only supports the initial creation of ``buildout.cfg``, so if you have already run ``plock`` once and you want to install add-ons you'll have to use ``-f`` to overwrite ``buildout.cfg``.

Pick a few interesting things and install them::

    $ plock plone -i "Products.PloneFormGen collective.plonetruegallery eea.facetednavigation"
    Creating virtualenv... (plone)
    Installing buildout...
    Downloading installer (https://launchpad.net/plone/4.3/4.3.4/+download/Plone-4.3.4-r1-UnifiedInstaller.tgz)
    Unpacking installer...
    Unpacking cache...
    Installing eggs...
    Installing cmmi & dist...
    Configuring cache...
    Installing addons...
    - https://pypi.python.org/pypi/Products.PloneFormGen
    - https://pypi.python.org/pypi/collective.plonetruegallery
    - https://pypi.python.org/pypi/eea.facetednavigation
    Running buildout...
    Done, now run:
      plone/bin/plone fg

Now you should see your add-ons available in Plone:

.. image:: /images/plock-screen-6.png
    :alt: Plock Screen 6
    :align: center
    :class: img-thumbnail

Upgrading Plone
~~~~~~~~~~~~~~~


Step #1
+++++++

Realize Plock has created a ``buildout.cfg`` file you can edit with a text editor.

Step #2
+++++++

Also realize Plock hosts `Buildout configuration files called Pins <https://github.com/plock/pins>`_ you can ``extend`` from your local ``buildout.cfg`` file [10]_.

Step #3
+++++++

Edit your ``buildout.cfg`` file. Change the first ``extends`` URL from::

    [buildout]
    extends =
        https://raw.github.com/plock/pins/master/plone-4-3
    #    https://raw.github.com/plock/pins/master/dev

To::

    [buildout]
    extends =
        https://raw.github.com/plock/pins/master/plone-5-0
    #    https://raw.github.com/plock/pins/master/dev

Run Buildout and start Plone::

    $ bin/buildout
    $ bin/plone fg

Enjoy the Plone 5 running man:

.. image:: /images/plock-screen-5.png
    :alt: Plock Screen 5
    :align: center
    :class: img-thumbnail

TL;DR
-----

Cut and paste this into a terminal::

    pip install plock; plock plone; plone/bin/plone fg

Now open http://localhost:8080 and happy Ploning.

*Plock 0.3.0 is out! Install with* ``pip install plock`` *and report issues here:* https://github.com/plock/plock/issues.

Footnotes
---------

.. [1] Whether or not dealing with the complexity is worth it, I will not address. Suffice it to say, plenty of folks still use and care about Plone and with a Plone 5 release pending, there is excitement building.

.. [2] He probably made it many times, and rightfully so.

.. [3] You can create an "instance" after ``pip install zope2`` with ``bin/mkzopeinstance`` but ``$INSTANCE/bin/runzope`` fails with ``ImportError: cannot import name _error_start`` probably due to mismanaged package versions. Maybe we can fix this with version specs included in a dummy package's ``setup.py``?

.. [4] The integration is *not* seemless, an undisputed fact as far as I know.

.. [5] 235

.. [7] Creating and executing a ``buildout.cfg`` file for the end user. Buildout configuration files are written in INI-style text. Ideally the end user sees this file and says "Ah, now I understand how this works."

.. [8] I've also `covered <http://blog.aclark.net/2013/07/19/introducing-plock/>`_ `Plock <http://blog.aclark.net/2013/07/29/whats-new-as-of-plock-0-1-2/>`_ `before <http://blog.aclark.net/2013/12/29/introducing-plock-again/>`_ `here <http://blog.aclark.net/2014/03/20/introducing-plock-pins/>`_.

.. [9] As someone familiar with Python and a UNIX shell already, because that is the market I like to serve.

.. [10] Yes, there is a security and/or reliability issue with doing this; you are clearly trading security and reliability for convenience.

.. raw:: html

    <br />
    <script data-gratipay-username="aclark4life" src="//grtp.co/v1.js"></script>
