First Post
==========

.. post:: 2007/03/16
    :category: Buildout, Plone, Python, Zope

**I have decided to start a blog**

|

.. image:: /images/look-at-me.jpg
    :align: center
    :class: img-thumbnail

|

Why? To show Plone can be used for blogging, but also:

- I have been reading a lot of `Plone blogs <http://planet.plone.org>`_ lately and they have inspired me to write my own.
- I want to interact with other Plone users.
- I want to use new technology.

To that end, this post is about my `build tools <http://svn.plone.org/svn/collective/newzope>`_. But first I'll note the current, likely better, alternatives:

- `Buildout <http://www.buildout.org>`_
- `Buildit <https://agendaless.com/software/Members/chrism/software/buildit/>`_
- `Instance Manager <https://old.plone.org/products/instance-manager>`_

I used Buildout for the first time at the `Baarn UI Sprint 2007 <https://old.plone.org/events/sprints/past-sprints/baarn-ui-sprint-2007>`_ and I've also used Chris McDonough's Buildit. There are even more to choose from, but for now I enjoy typing:

::

    newzope test-site ProductA ProductB ProductC

and having a working instance a few seconds later with Product{A,B,C} installed.
