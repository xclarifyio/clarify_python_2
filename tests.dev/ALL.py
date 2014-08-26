#!/usr/bin/python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
import bundle_create
import bundle_list
import bundle_update
import bundle_delete
import metadata_create
import metadata_update
import metadata_delete
import track_create
import track_delete
import search
import error


def all_tests(apikey=None):
    """Call all test functions."""

    bundle_create.all_tests(apikey)
    bundle_update.all_tests(apikey)
    bundle_list.all_tests(apikey)
    bundle_delete.all_tests(apikey)
    metadata_create.all_tests(apikey)
    metadata_update.all_tests(apikey)
    metadata_delete.all_tests(apikey)
    track_create.all_tests(apikey)
    track_delete.all_tests(apikey)
    search.all_tests(apikey)
    error.all_tests(apikey)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
