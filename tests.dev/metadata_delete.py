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

def delete():
    op3nvoice.set_key(ak)

    # Create a bundle with some metadata.
    data = {'wife': 'Medea', 'husband': 'Jason'}
    br = op3nvoice.create_bundle(name='metadata update test',
                                 metadata=data)

    # Retrieve the metadata and print it.
    m = op3nvoice.get_metadata(br['_links']['o3v:metadata']['href'])
    print_metadata_info(m)

    # Delete the metadata and print it.
    op3nvoice.delete_metadata(m['_links']['self']['href'])
    m = op3nvoice.get_metadata(br['_links']['o3v:metadata']['href'])
    print_metadata_info(m)

def print_metadata_info(m):
    print '** Bundle info'
    print '* Created: ' + m['created']
    print '* Updated: ' + m['updated']
    if m.has_key('data'):
        print '* Data: ' + str(m['data'])

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    delete()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
