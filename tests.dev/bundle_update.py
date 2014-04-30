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

def update_all_names():  ## Will fail if no bundles available.
    c = op3nvoice.Connection(ak)

    # Update all the names.
    has_next = True
    next_href = None # if None, retrieves first page
    while has_next:
        # Get a page and print content.
        _bl = op3nvoice.get_bundle_list(c, next_href)
        bl = op3nvoice_plus.BundleList(_bl)
        for i in bl.get_bundle_hrefs():
            update_name(c, i)
        # Setup for next possible page.
        if bl.has_next_href():
            next_href = bl.get_next_href()
        else:
            has_next = False

    # Print all the new names.
    has_next = True
    next_href = None # if None, retrieves first page
    while has_next:
        # Get a page and print content.
        _bl = op3nvoice.get_bundle_list(c, next_href)
        bl = op3nvoice_plus.BundleList(_bl)
        for i in bl.get_bundle_hrefs():
            print_name(c, i)
        # Setup for next possible page.
        if bl.has_next_href():
            next_href = bl.get_next_href()
        else:
            has_next = False
        
def update_name(conn, href):
    _b = op3nvoice.get_bundle(conn, href)
    b = op3nvoice_plus.Bundle(_b)
    name = b.get_name()
    if name == None:
        name = 'no name updated'
    else:
        name = name + ' updated'
        print 'Updating name for ' + href
    op3nvoice.update_bundle(conn, href, name)

def print_name(conn, href):
    _b = op3nvoice.get_bundle(conn, href)
    b = op3nvoice_plus.Bundle(_b)
    print href + ' is named ' + b.get_name()
    

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    update_all_names()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
