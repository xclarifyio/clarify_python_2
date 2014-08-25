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

def metadata_delete():
    clarify.set_key(ak)

    # Create a bundle with some metadata.
    print '*** Creating a bundle with mythical metadata...'
    data = {'wife': 'Medea', 'husband': 'Jason'}
    br = clarify.create_bundle(name='metadata update test',
                                 metadata=data)

    # Retrieve the metadata and print it.
    print '*** Retrieving metadata...'
    m = clarify.get_metadata(br['_links']['clarify:metadata']['href'])
    print_metadata_info_quiet(m)

    # Delete the metadata and print it.
    print '*** Deleting metadata...'
    clarify.delete_metadata(m['_links']['self']['href'])

    # Retrieve the metadata and print it.
    print '*** Retrieving metadata...'
    m = clarify.get_metadata(br['_links']['clarify:metadata']['href'])
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
    
    print '===== metadata_delete() ====='
    metadata_delete()

if __name__ == '__main__':

    set_appkey(sys.argv[1])
    
    all()
