#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from clarify_python_2 import clarify

ak = None # our app key.

def set_appkey(key):
    global ak
    ak = key

def create_15_bundles():
    clarify.set_key(ak)
    for i in range(0,15):
        br = clarify.create_bundle(str(i))
        href = br['_links']['self']['href']
        b = clarify.get_bundle(href)
        print '*** Created bundle ' + href + ' with name: ' + b['name']

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)

    print '===== create_15_bundles() ====='
    create_15_bundles()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
