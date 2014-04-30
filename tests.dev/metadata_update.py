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

def create_and_update():
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

    # Change the metadata and print it.
    data2 = {'wife': 'Clytemnestra', 'husband': ['Agamemnon', 'Aegisthus']}
    op3nvoice.update_metadata(c, m.get_self_href(), data2)
    _m = op3nvoice.get_metadata(c, m.get_self_href())
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
    
    create_and_update()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
