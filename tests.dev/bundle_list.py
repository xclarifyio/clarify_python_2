#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from clarify_python_2 import clarify
import common

ak = None # our app key.

def set_appkey(key):
    global ak
    ak = key

def get_first_page_hrefs():
    clarify.set_key(ak)

    bl = clarify.get_bundle_list()

    print '*** Available bundles: ' + str(bl['total'])
    print '*** Printing first page of hrefs retrieved (max 10)...'
    for i in bl['_links']['items']:
        print i['href']

def get_all_bundle_hrefs():    
    clarify.set_key(ak)

    print '*** Printing all available bundle hrefs...'
    common.bundle_list_map(print_href)
    
def get_all_bundles():
    clarify.set_key(ak)

    print '*** Printing all available bundle...'
    common.bundle_list_map(print_bundle)

def print_href(href):
    print href

def print_bundle(href):
    bundle = clarify.get_bundle(href)
    print '* Bundle ' + bundle['id'] + '...'
    if bundle.has_key('name'):
        print 'name: ' + bundle['name']
    if bundle.has_key('external_id'):
        print 'external_id: ' + bundle['external_id']
    if bundle.has_key('notify_url'):
        print 'notify_url: ' + bundle['notify_url']
    print 'created: ' + bundle['created']
    print 'updated: ' + bundle['updated']

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    print '===== get_first_page_hrefs() ====='
    get_first_page_hrefs()
    print '===== get_all_bundle_hrefs() ====='
    get_all_bundle_hrefs()
    print '===== get_all_bundles() ====='
    get_all_bundles()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
