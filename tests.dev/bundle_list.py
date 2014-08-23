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

def get_first_page():
    clarify.set_key(ak)

    bl = clarify.get_bundle_list()

    print '** total: ' + str(bl['total'])
    print '** Bundle hrefs start'
    for i in bl['_links']['items']:
        print i['href']
    print '** Bundle hrefs end'
    if bl['_links'].has_key('next'):
        print '** next: ' + bl['_links']['next']['href']
    if bl['_links'].has_key('previous'):
        print '** next: ' + bl['_links']['previous']['href']
    print '** first: ' + bl['_links']['first']['href']
    print '** last: ' + bl['_links']['last']['href']

def get_all_bundle_hrefs():    
    clarify.set_key(ak)
    common.bundle_list_map(print_href)
    
def get_all_bundles():
    clarify.set_key(ak)
    common.bundle_list_map(print_bundle)

def print_href(href):
    print href

def print_bundle(href):
    bundle = clarify.get_bundle(href)
    print '** Bundle...'
    print 'id: ' + bundle['id']
    if bundle.has_key('name'):
        print 'name: ' + bundle['name']
    print 'created: ' + bundle['created']
    print 'updated: ' + bundle['updated']

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    get_first_page()
    get_all_bundle_hrefs()
    get_all_bundles()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
