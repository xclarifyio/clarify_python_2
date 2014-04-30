====
TODO
====

Structural
----------

* PIP packaging (https://github.com/audreyr/cookiecutter-pypackage)
* Implement Scrutinizer
* Separate REST library and PLUS library.

Documentation
-------------

* Change all documentation to be rst-friendly for sphinx.

Tests
-----

* Base function unit tests.
* Test retrieving embedded item when count == 1.

Examples
--------

* Getting started guide.
* Examples to match PHP examples.
* Retrieving and processing YouTube channel.

Features
--------

* Python objects that return dates should return datetimes.

Implementation
--------------

* Modify embed list handling to match new system (bundle lists & search).
* Intialize Bundle() with an href and have it call get_bundle(href)?
* In utils, generic named process_embed() maybe should be
  process_bundle_collection embed or something. When we have different
  types of models we'll have different embeds. We will also have
  collections of other things -- apps for example.
* Pull version info from op3nvoice.__VERSION__


