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
MEDIA_URL3 = 'http://204.45.41.186/33/music/hindi/movies/1995/o/oh_darling_yeh_hai_india/Public-Ko-Hasao_(webmusic.in).mp3'


def delete_track_using_index():
    """Delete a track using the track index."""

    # Create a bundle with no track.
    print '*** Creating a bundle with no tracks...'
    bundle_ref = clarify.create_bundle(name='track tester')
    href = bundle_ref['_links']['clarify:tracks']['href']

    # Add three tracks.
    print '*** Adding a track to the bundle...'
    clarify.create_track(href, media_url=MEDIA_URL1, label='first label')
    print '*** Adding a track to the bundle...'
    clarify.create_track(href, media_url=MEDIA_URL2, label='second label')
    print '*** Adding a track to the bundle...'
    clarify.create_track(href, media_url=MEDIA_URL3, label='third label')

    # List the tracks.
    track_list = clarify.get_track_list(href)
    for track in track_list['tracks']:
        print_track_quiet(track)

    # Delete the track at index 1.
    print '*** Deleting the second track (index 1)...'
    clarify.delete_track_at_index(href, index=1)

    # List the tracks.
    track_list = clarify.get_track_list(href)
    for track in track_list['tracks']:
        print_track_quiet(track)


def delete_all_tracks():
    """Create a bundle, add tracks, delete them."""

    # Create a bundle with no track.
    print '*** Creating a bundle with no tracks...'
    bundle_ref = clarify.create_bundle(name='track tester')
    href = bundle_ref['_links']['clarify:tracks']['href']

    # Add three tracks.
    print '*** Adding a track to the bundle...'
    clarify.create_track(href, media_url=MEDIA_URL1, label='first label')
    print '*** Adding a track to the bundle...'
    clarify.create_track(href, media_url=MEDIA_URL2, label='second label')
    print '*** Adding a track to the bundle...'
    clarify.create_track(href, media_url=MEDIA_URL3, label='third label')

    # List the tracks.
    track_list = clarify.get_track_list(href)
    for track in track_list['tracks']:
        print_track_quiet(track)

    # Update the track.
    print '*** Deleting all tracks...'
    clarify.delete_track_at_index(href)

    # List the tracks.
    track_list = clarify.get_track_list(href)
    for track in track_list['tracks']:
        print_track_quiet(track)


def delete_track_using_href():
    """Delete a track using its href."""

    # Create a bundle with no track.
    print '*** Creating a bundle with no tracks...'
    bundle_ref = clarify.create_bundle(name='track tester')
    href = bundle_ref['_links']['clarify:tracks']['href']

    # Add a track.
    print '*** Adding a track to the bundle...'
    track_ref = clarify.create_track(href, media_url=MEDIA_URL1,
                                     label='short-lived track')

    # List the tracks.
    track_list = clarify.get_track_list(href)
    for track in track_list['tracks']:
        print_track_quiet(track)

    # Delete the track.
    print '*** Deleting track by href...'
    track_href = track_ref['_links']['self']['href']
    clarify.delete_track(track_href)

    # List the tracks.
    track_list = clarify.get_track_list(href)
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

    print 'id/index: ' + track['id'] + ' / ' + str(track['track'])


def all_tests(apikey):
    """Set API key and call all test functions."""

    clarify.set_key(apikey)

    print '===== delete_track_using_index() ====='
    delete_track_using_index()
    print '===== delete_all_tracks() ====='
    delete_all_tracks()
    print '===== delete_track_using_href() ====='
    delete_track_using_href()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <apikey>'
        exit(1)

    all_tests(sys.argv[1])
