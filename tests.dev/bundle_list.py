#!/usr/bin/python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
sys.path.insert(0, '..')
from clarify_python_2 import clarify
import common

def get_first_page_hrefs():
    """Print first page of bundle hrefs."""

    bundle_list = clarify.get_bundle_list()

    print '*** Available bundles: ' + str(bundle_list['total'])
    print '*** Printing first page of hrefs retrieved (max 10)...'
    for i in bundle_list['_links']['items']:
        print i['href']


def get_all_bundle_hrefs():
    """Print all bundle hrefs."""

    print '*** Printing all available bundle hrefs...'
    common.bundle_list_map(print_href)


def get_all_bundles():
    """Print all bundles."""

    print '*** Printing all available bundle...'
    common.bundle_list_map(print_bundle)


def print_href(href):
    """Function to print an href."""

    print href


def print_bundle(href):
    """Function to print an bundle from an href."""

    bundle = clarify.get_bundle(href)
    print '* Bundle ' + bundle['id'] + '...'
    if 'name' in bundle:
        print 'name: ' + bundle['name']
    if 'external_id' in bundle:
        print 'external_id: ' + bundle['external_id']
    if 'notify_url' in bundle:
        print 'notify_url: ' + bundle['notify_url']
    print 'created: ' + bundle['created']
    print 'updated: ' + bundle['updated']


def all_tests(apikey):
    """Set API key and call all test functions."""

    clarify.set_key(apikey)

    print '===== get_first_page_hrefs() ====='
    get_first_page_hrefs()
    print '===== get_all_bundle_hrefs() ====='
    get_all_bundle_hrefs()
    print '===== get_all_bundles() ====='
    get_all_bundles()


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
