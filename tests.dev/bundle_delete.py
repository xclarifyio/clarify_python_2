#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from op3nvoice_python_2 import op3nvoice
import common

ak = None # our app key.

def set_appkey(key):
    global ak
    ak = key

def delete_bundle(href):
    print 'Deleting ' + href
    op3nvoice.delete_bundle(href)

def delete_all():
    op3nvoice.set_key(ak)
    common.bundle_list_map(delete_bundle)

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    delete_all()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
