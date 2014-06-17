#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from op3nvoice_python_2 import op3nvoice

ak = None # our app key.

def set_appkey(key):
    global ak
    ak = key

def create_11():
    op3nvoice.set_key(ak)
    for i in range(0,11):
        br = op3nvoice.create_bundle(str(i))
        href = br['_links']['self']['href']
        b = op3nvoice.get_bundle(href)
        print 'Created bundle ' + href + ' with name: ' + b['name']

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    create_11()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
