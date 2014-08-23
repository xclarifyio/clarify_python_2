#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from clarify_python_2 import clarify
from clarify_python_2 import __api_version__

ak = None # our app key.


def set_appkey(key):
    global ak
    ak = key

def process_exception():
    clarify.set_key(ak)

    try:
        bad_href = '/' + __api_version__ + '/' + \
                   clarify.BUNDLES_PATH + '/' + 'bozo'
        clarify.get_bundle(href=bad_href)
    except clarify.APIException, e:
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
