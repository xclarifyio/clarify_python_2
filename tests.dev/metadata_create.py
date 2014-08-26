#!/usr/bin/python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
sys.path.insert(0, '..')
from clarify_python_2 import clarify

def metadata_create():
    """Create metadata and create a bundle with it."""

    # Create a bundle with metadata.
    # Note that all examples below are valid.
    print '*** Creating a bundle with mythical metadata...'
    data = {'wife': 'Medea', 'husband': 'Jason'}
    # data = {'wife': 'Medea', 'lovers': ['Aegisthus', 'Pancreon']}
    # data = {'daughters': 1, 'sons': 3}
    # data = {'hot': True, 'cold': False, 'tepid': None}
    bundle_ref = clarify.create_bundle(name='md test', metadata=data)

    #
    # 3 different ways to retrieve our metadata!
    #

    # (1) Retrieve the metadata from bundle reference.  Print it.
    print '*** Retrieving metadata from bundle reference...'
    href = bundle_ref['_links']['clarify:metadata']['href']
    metadata = clarify.get_metadata(href)
    print_metadata_info_quiet(metadata)

    # (2) Retrieve the bundle, then retrieve the metadata.  Print it.
    print '*** Retrieving the bundle then the metadata...'
    href = clarify.get_bundle(bundle_ref['_links']['self']['href'])
    metadata = clarify.get_metadata(href['_links']['clarify:metadata']['href'])
    print_metadata_info_quiet(metadata)

    # (3) Retrieve the bundle with the metadata embedded.  Print it.
    print '*** Retrieving the bundle with embedded metadata...'
    href = clarify.get_bundle(bundle_ref['_links']['self']['href'],
                              embed_metadata=True)
    metadata = href['_embedded']['clarify:metadata']
    print_metadata_info_quiet(metadata)


def print_metadata_info(metadata):
    """Print metadata."""

    print '** Metadata info'
    print '* Created: ' + metadata['created']
    print '* Updated: ' + metadata['updated']
    if 'data' in metadata:
        print '* Data: ' + str(metadata['data'])


def print_metadata_info_quiet(metadata):
    """Print condensed version of metadata."""

    if 'data' in metadata:
        print str(metadata['data'])


def all_tests(apikey):
    """Set API key and call all test functions."""

    clarify.set_key(apikey)

    print '===== metadata_create() ====='
    metadata_create()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
