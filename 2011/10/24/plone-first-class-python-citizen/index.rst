Plone: First Class Python Citizen
=================================

.. post:: 2011/10/24
    :category: Plone, Python

**The Plone community and software fit nicely within the larger Python ecosystem. Here's why.**

For almost as long as I have been involved in the `Plone`_ project, I've been interested in Plone's role in the Python ecosystem. Today as I look across the current landscape, I'm proud to announce a new milestone the Plone community can take pride in. But the change didn't happen overnight, so first let's take a quick look back.

PyPI support in PSC
-------------------

Circa 2008, Tarek Ziadé and others finished the PyPI integration branch of PloneSoftwareCenter started by Sidnei Da Silva 2 years before.

This was a big step towards the "Pythonification" of Plone, mainly because Plone packages could now be published on plone.org in the same way Python packages are published to the Python Package Index: via "python setup.py upload". In fact if you are publishing Plone packages, it is recommended that you release to *both* PyPI and plone.org simultaneously. This ensures your package is visible to the most number of potential users. And you can use `mkrelease`_ to automate the process.

Collective docs at RTD
----------------------

Just when you thought things couldn't get more exciting in Python land, along came `readthedocs.org`_ (a Django Dash production, IIRC). And to `join the fun in July 2011`_, I moved Mikko Ohtamaa's awesome **Plone Community Managed Developer Manual** to the `Github collective`_ and configured the RTD `service hook`_.

This means that whenever anyone commits a change to the developer manual, within a few minutes a new Sphinx build `gets published`_. It was so easy to set this up, I wish I had done it sooner.

So you can that see over the years, we have been working ourselves into a frenzy of Python goodness! And last week, it got even better.

Introducing: Plone packages!
----------------------------

Thanks to the good folks at `Cartwheel Web`_, makers of the fine `Open Comparison`_ service, Plone now has its very own `grid comparison website`_! (`Djangopackages.com`_ was first, followed by `pyramid.opencomparison.org`_.)

This is a site where folks can add packages hosted elsewhere (e.g. svn, github, pypi), vote on them, and add grid comparisons to compare similarly-featured add-ons, frameworks, and other related software.  Grids are the killer feature of this site, and personally I've been waiting to use them to answer questions like:

    **Q: What's the best blogging add-on for Plone?**

    **A: http://plone.opencomparison.org/grids/g/weblogs/**

The content is entirely user driven (TTW only) so please head over to `plone.opencomparison.org`_, login with your github ID, and start adding packages! And while you are at it, please report any issues you find here: `https://github.com/opencomparison/opencomparison/issues`_. Lastly, let's all tweet a big thanks to `@pydanny`_\ and `@audreyr`_ for their hard work and generosity!

.. _Plone: http://plone.org
.. _mkrelease: http://pypi.python.org/pypi/jarn.mkrelease
.. _readthedocs.org: http://readthedocs.org/
.. _join the fun in July 2011: https://github.com/collective/collective.developermanual/commit/4dc34d113b1a62064c83f3c431acc7d8deb42f1a
.. _Github collective: http://github.com/collective
.. _service hook: https://github.com/blog/41-service-integration
.. _gets published: http://collective-docs.readthedocs.org/en/latest/index.html
.. _Cartwheel Web: http://www.cartwheelweb.com/
.. _Open Comparison: http://opencomparison.org/
.. _grid comparison website: http://plone.opencomparison.org
.. _Djangopackages.com: http://djangopackages.com
.. _pyramid.opencomparison.org: http://pyramid.opencomparison.org
.. _plone.opencomparison.org: http://plone.opencomparison.org
.. _`https://github.com/opencomparison/opencomparison/issues`: https://github.com/opencomparison/opencomparison/issues
.. _@pydanny: https://twitter.com/#!/pydanny
.. _@audreyr: https://twitter.com/#!/audreyr
