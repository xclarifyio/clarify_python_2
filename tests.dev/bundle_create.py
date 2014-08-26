#!/usr/bin/python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
sys.path.insert(0, '..')
from clarify_python_2 import clarify


def create_15_bundles():
    """Create 15 bundles without any media."""

    for i in range(0, 15):
        bundle_ref = clarify.create_bundle(str(i))
        href = bundle_ref['_links']['self']['href']
        bundle = clarify.get_bundle(href)
        print '*** Created bundle ' + href + ' with name: ' + bundle['name']


def all_tests(apikey):
    """Set API key and call all test functions."""

    clarify.set_key(apikey)

    print '===== create_15_bundles() ====='
    create_15_bundles()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
