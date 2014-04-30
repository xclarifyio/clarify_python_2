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

def delete_all():
    c = op3nvoice.Connection(ak)

    # Delete all bundles.
    has_next = True
    next_href = None # if None, retrieves first page
    while has_next:
        # Get a page and print content.
        _bl = op3nvoice.get_bundle_list(c, next_href)
        bl = op3nvoice_plus.BundleList(_bl)
        for i in bl.get_bundle_hrefs():
            print '** Deleting ' + i
            op3nvoice.delete_bundle(c, i)
            
        # Setup for next possible page.
        if bl.has_next_href():
            next_href = bl.get_next_href()
        else:
            has_next = False

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    delete_all()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
