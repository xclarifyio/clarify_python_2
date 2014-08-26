#!/usr/bin/python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
sys.path.insert(0, '..')
from clarify_python_2 import clarify
import common

def delete_bundle(href):
    """Delete bundle at href."""

    print '*** Deleting ' + href
    clarify.delete_bundle(href)


def delete_all_bundles():
    """Delete all bundles."""

    common.bundle_list_map(delete_bundle)


def all_tests(apikey):
    """Set API key and call all test functions."""

    clarify.set_key(apikey)

    print '===== delete_all_bundles() ====='
    delete_all_bundles()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
