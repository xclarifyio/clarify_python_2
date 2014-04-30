#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from op3nvoice_python_2 import op3nvoice
from op3nvoice_python_2 import op3nvoice_plus

ak = None # our app key.

def set_appkey(key):
    global ak
    ak = key

def get_first_page():
    c = op3nvoice.Connection(ak)

    _bl = op3nvoice.get_bundle_list(c)
    bl = op3nvoice_plus.BundleList(_bl)

    print '** total: ' + str(bl.get_total())
    print_bundle_refs(bl)
    if bl.has_next_href():
        print '** next: ' + bl.get_next_href()
    if bl.has_previous_href():
        print '** next: ' + bl.get_previous_href()
    print '** first: ' + bl.get_first_href()
    print '** last: ' + bl.get_last_href()

def get_all_bundle_hrefs():    
    c = op3nvoice.Connection(ak)

    has_next = True
    next_href = None # if None, retrieves first page

    while has_next:
        _bl = op3nvoice.get_bundle_list(c, next_href)
        bl = op3nvoice_plus.BundleList(_bl)
        print_bundle_refs(bl)
        if bl.has_next_href():
            next_href = bl.get_next_href()
        else:
            has_next = False

def get_all_bundles():
    c = op3nvoice.Connection(ak)

    has_next = True
    next_href = None # if None, retrieves first page

    while has_next:
        # Get a page and print content.
        _bl = op3nvoice.get_bundle_list(c, next_href, embed_items=True)
        bl = op3nvoice_plus.BundleList(_bl)
        for i in bl.get_bundles():
            print_bundle(op3nvoice_plus.Bundle(i))
        # Setup for next possible page.
        if bl.has_next_href():
            next_href = bl.get_next_href()
        else:
            has_next = False
        
def print_bundle_refs(bundle_list):
    print '** Bundle hrefs start'
    for i in bundle_list.get_bundle_hrefs():
        print i
    print '** Bundle hrefs end'

def print_bundle(bundle):
    print '** Bundle...'
    print 'id: ' + bundle.get_id()
    name = bundle.get_name()
    if name != None:
        print 'name: ' + name
    print 'created: ' + bundle.get_created()
    print 'updated: ' + bundle.get_updated()

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    get_first_page()
    get_all_bundle_hrefs()
    get_all_bundles()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
