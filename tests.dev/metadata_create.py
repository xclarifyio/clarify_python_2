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

def simple_create():
    clarify.set_key(ak)

    # Create a bundle with metadata.
    # Note that all examples below are valid.
    data = {'wife': 'Medea', 'husband': 'Jason'}
    # data = {'wife': 'Medea', 'lovers': ['Aegisthus', 'Pancreon']}
    # data = {'daughters': 1, 'sons': 3}
    # data = {'hot': True, 'cold': False, 'tepid': None}
    br = clarify.create_bundle(name='md test', metadata=data)

    ## 3 different ways to retrieve our metadata!

    # (1) Retrieve the metadata from bundle reference.  Print it.
    href = br['_links']['clarify:metadata']['href']
    m = clarify.get_metadata(href)
    print_metadata_info(m)

    # (2) Retrieve the bundle, then retrieve the metadata.  Print it.
    b = clarify.get_bundle(br['_links']['self']['href'])
    m = clarify.get_metadata(b['_links']['clarify:metadata']['href'])
    print_metadata_info(m)

    # (3) Retrieve the bundle with the metadata embedded.  Print it.
    b = clarify.get_bundle(br['_links']['self']['href'],
                             embed_metadata=True)
    m = b['_embedded']['clarify:metadata']
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
    
    simple_create()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
