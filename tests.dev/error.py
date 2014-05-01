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

def process_exception():
    c = op3nvoice.Connection(ak)

    try:
        bad_href = '/' + op3nvoice.API_VERSION + '/' + \
                   op3nvoice.BUNDLES_PATH + '/' + 'bozo'
        op3nvoice.get_bundle(c, href=bad_href)
    except op3nvoice.APIException, e:
        print '** Caught APIException'
        print 'code = ' + str(e.get_code())
        print 'status = ' + e.get_status()
        print 'message = ' + e.get_message()


def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)

    process_exception()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
