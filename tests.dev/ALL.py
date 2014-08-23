#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.  These tests are designed to be run interactively.
##

import sys
import bundle_create
import bundle_list
import bundle_update
import bundle_delete
import metadata_create
import metadata_delete
import metadata_update
import track_create
import track_delete
import search
import error

ak = None # our app key.

def set_appkey(key):
    global ak
    ak = key

def all(_ak=None):
    
    bundle_create.all(ak)
    bundle_update.all(ak)
    bundle_list.all(ak)
    bundle_delete.all(ak)
    metadata_create.all(ak)
    metadata_update.all(ak)
    metadata_delete.all(ak)
    track_create.all(ak)
    track_delete.all(ak)
    search.all(ak)
    error.all(ak)

if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
    
