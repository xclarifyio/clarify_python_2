#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from clarify_python_2 import clarify

ak = None # our app key.

MEDIA_URL1 = 'http://www.kqed.org/.stream/anon/radio/hd/2008/09/2008-09-18c-hd.mp3'
MEDIA_URL2 = 'http://feedproxy.google.com/~r/kqed/ClimateWatch/~5/UTaeFBdvZSw/2012-05-04a-tcr.mp3'
MEDIA_URL3 = 'http://204.45.41.186/33/music/hindi/movies/1995/o/oh_darling_yeh_hai_india/Public-Ko-Hasao_(webmusic.in).mp3'

def set_appkey(key):
    global ak
    ak = key

def delete_track_using_index():
    clarify.set_key(ak)

    # Create a bundle with no track.
    print '*** Creating a bundle with no tracks...'
    br = clarify.create_bundle(name='track tester')
    href = br['_links']['clarify:tracks']['href']

    # Add three tracks.
    print '*** Adding a track to the bundle...'
    r = clarify.create_track(href,
                               media_url=MEDIA_URL1, label='first label')
    print '*** Adding a track to the bundle...'
    r = clarify.create_track(href,
                               media_url=MEDIA_URL2, label='second label')
    print '*** Adding a track to the bundle...'
    r = clarify.create_track(href,
                               media_url=MEDIA_URL3, label='third label')
                       
    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track_quiet(i)

    # Delete the track at index 1.
    print '*** Deleting the second track (index 1)...'
    r = clarify.delete_track_at_index(href, index=1)

    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track_quiet(i)

def delete_all_tracks():
    clarify.set_key(ak)

    # Create a bundle with no track.
    print '*** Creating a bundle with no tracks...'
    br = clarify.create_bundle(name='track tester')
    href = br['_links']['clarify:tracks']['href']

    # Add three tracks.
    print '*** Adding a track to the bundle...'
    r = clarify.create_track(href,
                               media_url=MEDIA_URL1, label='first label')
    print '*** Adding a track to the bundle...'
    r = clarify.create_track(href,
                               media_url=MEDIA_URL2, label='second label')
    print '*** Adding a track to the bundle...'
    r = clarify.create_track(href,
                               media_url=MEDIA_URL3, label='third label')
                       
    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track_quiet(i)

    # Update the track.
    print '*** Deleting all tracks...'
    r = clarify.delete_track_at_index(href)

    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track_quiet(i)

def delete_track_using_href():

    # Create a bundle with no track.
    print '*** Creating a bundle with no tracks...'
    br = clarify.create_bundle(name='track tester')
    href = br['_links']['clarify:tracks']['href']

    # Add a track.
    print '*** Adding a track to the bundle...'
    r = clarify.create_track(href, media_url=MEDIA_URL1, label='short-lived track')

    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track_quiet(i)

    # Delete the track.
    print '*** Deleting track by href...'
    track_href = r['_links']['self']['href']
    r = clarify.delete_track(track_href)

    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track_quiet(i)


def print_track(track):

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
    print 'id/index: ' + track['id'] + ' / ' + str(track['track'])

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)

    print '===== delete_track_using_index() ====='
    delete_track_using_index()
    print '===== delete_all_tracks() ====='
    delete_all_tracks()
    print '===== delete_track_using_href() ====='
    delete_track_using_href()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
