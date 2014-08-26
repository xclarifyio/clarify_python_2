#!/usr/bin/python

"""
Some test functions used to sanity check during development. Not
unit tests.
"""

import sys
sys.path.insert(0, '..')
from clarify_python_2 import clarify

MEDIA_URL1 = 'http://www.kqed.org/.stream/anon/radio/hd/2008/09/2008-09-18c-hd.mp3'
MEDIA_URL2 = 'http://feedproxy.google.com/~r/kqed/ClimateWatch/~5/UTaeFBdvZSw/2012-05-04a-tcr.mp3'


def track_create_and_list():
    """Create a bundle with a track, print it, add a track, print them."""

    print '*** Creating a bundle with a track...'

    # Create a bundle with a track.
    bundle_ref = clarify.create_bundle(name='track tester',
                                       media_url=MEDIA_URL1)

    # List the tracks.
    track_list_ref = bundle_ref['_links']['clarify:tracks']['href']
    track_list = clarify.get_track_list(track_list_ref)
    for track in track_list['tracks']:
        print_track_quiet(track)

    print '*** Adding a track to the bundle...'

    # Add a track.
    clarify.create_track(track_list_ref, media_url=MEDIA_URL2)

    # List the tracks.
    track_list = clarify.get_track_list(track_list_ref)
    for track in track_list['tracks']:
        print_track_quiet(track)


def print_track(track):
    """Print a track."""

    print '** Track '
    print 'id: ' + track['id']
    print 'index: ' + str(track['track'])
    print 'label: ' + track['label']
    print 'media_url: ' + track['media_url']
    print 'audio_channel: ' + track['audio_channel']
    print 'audio_language: ' + track['audio_language']
    print 'created: ' + track['created']
    print 'updated: ' + track['updated']
    print 'status: ' + track['status']
    print 'mime_type: ' + track['mime_type']
    print 'media size: ' + str(track['media_size'])
    print 'duration: ' + str(track['duration'])
    print 'fetch_response_code: ' + str(track['fetch_response_code'])
    print 'fetch_response_message: ' + track['fetch_response_message']
    print 'media_code: ' + str(track['media_code'])
    print 'media_message: ' + track['media_message']


def print_track_quiet(track):
    """Print condensed version of track."""

    print 'id/index/url: ' + track['id'] + ' / ' + str(track['track']) + \
          ' / ' + track['media_url']


def all_tests(apikey):
    """Set API key and call all test functions."""

    clarify.set_key(apikey)

    print '===== track_create_and_list() ====='
    track_create_and_list()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
