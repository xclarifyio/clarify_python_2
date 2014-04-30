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

def create_26():
    c = op3nvoice.Connection(ak)
    for i in range(0,26):
        _br = op3nvoice.create_bundle(c, str(i))
        br = op3nvoice_plus.BundleReference(_br)
        _b = op3nvoice.get_bundle(c, br.get_self_href())
        b = op3nvoice_plus.Bundle(_b)
        print 'Created bundle with name: ' + b.get_name()

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    create_26()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
