#!/usr/bin/python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
sys.path.insert(0, '..')
from clarify_python_2 import clarify
from clarify_python_2 import __api_version__

def process_exception():
    """Create an exception, capture it, print it."""

    try:
        print '*** Generating an error...'
        bad_href = '/' + __api_version__ + '/' + \
                   clarify.BUNDLES_PATH + '/' + 'bozo'
        clarify.get_bundle(href=bad_href)
    except clarify.APIException, exception:
        print '*** Caught APIException'
        print 'code = ' + str(exception.get_code())
        print 'status = ' + exception.get_status()
        print 'message = ' + exception.get_message()


def all_tests(apikey):
    """Set API key and call all test functions."""

    clarify.set_key(apikey)

    print '===== process_exception() ====='
    process_exception()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
