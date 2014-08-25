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

def simple_search():
    """This function performs no setup, so we don't even check the
    results.  Just a basic sanity check."""

    clarify.set_key(ak)

    print '*** Searching for "father"...'
    print clarify.search(None, 'father')


def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)

    print '===== simple_search() ====='
    simple_search()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
