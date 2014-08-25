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

def create_and_update():
    clarify.set_key(ak)

    # Create a bundle with some metadata.
    print '*** Creating a bundle with mythical metadata...'
    data = {'wife': 'Medea', 'husband': 'Jason'}
    br = clarify.create_bundle(name='metadata update test',
                                 metadata=data)

    # Retrieve the metadata and print it.
    print '*** Retrieving metadata...'
    href = br['_links']['clarify:metadata']['href']
    m = clarify.get_metadata(href)
    print_metadata_info_quiet(m)

    # Change the metadata 
    print '*** Changing metadata...'
    data2 = {'wife': 'Clytemnestra', 'husband': ['Agamemnon', 'Aegisthus']}
    clarify.update_metadata(href, data2)

    # Retrieve the metadata and print it.
    print '*** Retrieving metadata...'
    m = clarify.get_metadata(href)
    print_metadata_info_quiet(m)

def print_metadata_info(m):
    print '** Bundle info'
    print '* Created: ' + m['created']
    print '* Updated: ' + m['updated']
    if m.has_key('data'):
        print '* Data: ' + str(m['data'])

def print_metadata_info_quiet(m):
    if m.has_key('data'):
        print str(m['data'])

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    print '===== create_and_update() ====='
    create_and_update()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
