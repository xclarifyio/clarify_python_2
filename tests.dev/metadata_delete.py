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

def delete():
    c = op3nvoice.Connection(ak)

    # Create a bundle with some metadata.
    data = {'wife': 'Medea', 'husband': 'Jason'}
    _br = op3nvoice.create_bundle(c, name='metadata update test',
                                  metadata=data)
    br = op3nvoice_plus.BundleReference(_br)

    # Retrieve the metadata and print it.
    _m = op3nvoice.get_metadata(c, br.get_metadata_href())
    m = op3nvoice_plus.Metadata(_m)
    print_metadata_info(m)

    # Delete the metadata and print it.
    op3nvoice.delete_metadata(c, m.get_self_href())
    _m = op3nvoice.get_metadata(c, m.get_self_href())
    m = op3nvoice_plus.Metadata(_m)
    print_metadata_info(m)

def print_metadata_info(m):
    print '** Bundle info'
    print '* Created: ' + m.get_created()
    print '* Updated: ' + m.get_updated()
    if m.has_data():
        print '* Data: ' + str(m.get_data())
    else:
        print '* Data: NO DATA AVAILABLE.'

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    delete()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
