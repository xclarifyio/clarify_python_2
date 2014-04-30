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

def simple_search():
    """This function performs no setup, so we don't even check the
    results.  Just a basic sanity check."""

    c = op3nvoice.Connection(ak)

    print op3nvoice.search(c, None, 'father')


def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)

    simple_search()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
