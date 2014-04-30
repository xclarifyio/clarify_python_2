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

def simple_create():
    c = op3nvoice.Connection(ak)

    # Create a bundle with metadata.
    # Note that all examples below are valid.
    data = {'wife': 'Medea', 'husband': 'Jason'}
    # data = {'wife': 'Medea', 'lovers': ['Aegisthus', 'Pancreon']}
    # data = {'daughters': 1, 'sons': 3}
    # data = {'hot': True, 'cold': False, 'tepid': None}
    _br = op3nvoice.create_bundle(connection=c, name='md test',
                                  metadata=data)
    br = op3nvoice_plus.BundleReference(_br)

    ## 3 different ways to retrieve our metadata!

    # (1) Retrieve the metadata from bundle reference.  Print it.
    _m = op3nvoice.get_metadata(c, br.get_metadata_href())
    m = op3nvoice_plus.Metadata(_m)
    print_metadata_info(m)

    # (2) Retrieve the bundle, then retrieve the metadata.  Print it.
    _b = op3nvoice.get_bundle(c, br.get_self_href())
    b = op3nvoice_plus.Bundle(_b)
    _m = op3nvoice.get_metadata(c, b.get_metadata_href())
    m = op3nvoice_plus.Metadata(_m)
    print_metadata_info(m)

    # (3) Retrieve the bundle with the metadata embedded.  Print it.
    _b = op3nvoice.get_bundle(c, br.get_self_href(), embed_metadata=True)
    b = op3nvoice_plus.Bundle(_b)
    _m = b.get_metadata()
    m = op3nvoice_plus.Metadata(_m)
    print_metadata_info(m)

def print_metadata_info(m):
    print '** Bundle info'
    print '* Created: ' + m.get_created()
    print '* Updated: ' + m.get_updated()
    if m.has_data():
        print '* Data: ' + str(m.get_data())

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    simple_create()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
