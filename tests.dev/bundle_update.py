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

def update_all_names():  ## Will fail if no bundles available.
    op3nvoice.set_key(ak)
    common.bundle_list_map(update_name)
    common.bundle_list_map(print_name)
        
def update_name(href):
    b = op3nvoice.get_bundle(href)
    name = b.get('name')
    if name == None:
        name = 'no name updated'
    else:
        name = name + ' updated'
        print 'Updating name for ' + href
    op3nvoice.update_bundle(href, name)

def print_name(href):
    b = op3nvoice.get_bundle(href)
    print href + ' is named ' + b['name']
    

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    update_all_names()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
