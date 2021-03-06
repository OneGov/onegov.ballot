Onegov Ballot
=============

Votes and elections for OneGov.

Models
------

.. image:: https://raw.githubusercontent.com/OneGov/onegov.ballot/master/docs/onegov.ballot.election.png
.. image:: https://raw.githubusercontent.com/OneGov/onegov.ballot/master/docs/onegov.ballot.vote.png


Domain of Influcence
--------------------

The domain of influence is based on the ``eCH-0155`` standard and used in
``onegov.ballot`` elections/votes and in ``onegov.election_day`` principals.

============== ====================== ============ ======================
eCH-0155       DomainOfInfluenceMixin Principal    Identifier
============== ====================== ============ ======================
CH: Bund       federation
CT: Kanton     canton                 Canton       Shortcut (``be``, ...)
BZ: Bezirk     region
MU: Gemeinde   municipality           Municipality BFS number
SK: Stadtkreis                                     District ID
============== ====================== ============ ======================

Run the Tests
-------------

Install tox and run it::

    pip install tox
    tox

Limit the tests to a specific python version::

    tox -e py27

Conventions
-----------

Onegov Ballot follows PEP8 as close as possible. To test for it run::

    tox -e pep8

Onegov Ballot uses `Semantic Versioning <http://semver.org/>`_

Build Status
------------

.. image:: https://travis-ci.org/OneGov/onegov.ballot.png?branch=master
  :target: https://travis-ci.org/OneGov/onegov.ballot
  :alt: Build Status

Coverage
--------

.. image:: https://coveralls.io/repos/OneGov/onegov.ballot/badge.png?branch=master
  :target: https://coveralls.io/r/OneGov/onegov.ballot?branch=master
  :alt: Project Coverage

Latests PyPI Release
--------------------
.. image:: https://img.shields.io/pypi/v/onegov.ballot.svg
  :target: https://pypi.python.org/pypi/onegov.ballot
  :alt: Latest PyPI Release


License
-------
onegov.ballot is released under GPLv2
