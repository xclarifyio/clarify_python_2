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

def set_appkey(key):
    global ak
    ak = key

def track_create_and_list():
    clarify.set_key(ak)

    print '*** Creating a bundle with a track...'

    # Create a bundle with a track.
    br = clarify.create_bundle(name='track tester', media_url=MEDIA_URL1)

    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

    print '*** Adding a track to the bundle...'

    # Add a track.
    r = clarify.create_track(br['_links']['clarify:tracks']['href'],
                               media_url=MEDIA_URL2)
                       
    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

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
              
def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    track_create_and_list()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
