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

def delete_1_track():
    clarify.set_key(ak)

    print '*** Creating a bundle with no tracks...'
    print '*** Adding a track to the bundle...'
    print '*** Adding a track to the bundle...'
    print '*** Adding a track to the bundle...'

    # Create a bundle with no track.
    br = clarify.create_bundle(name='track tester')
    href = br['_links']['clarify:tracks']['href']

    # Add three tracks.
    r = clarify.create_track(href,
                               media_url=MEDIA_URL1, label='first label')
    r = clarify.create_track(href,
                               media_url=MEDIA_URL2, label='second label')
    r = clarify.create_track(href,
                               media_url=MEDIA_URL3, label='third label')
                       
    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

    print '*** Deleting the second track (index 1)...'

    # Update the track.
    r = clarify.delete_track(href, track=1)

    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

def delete_all_tracks():
    clarify.set_key(ak)

    print '*** Creating a bundle with no tracks...'
    print '*** Adding a track to the bundle...'
    print '*** Adding a track to the bundle...'
    print '*** Adding a track to the bundle...'

    # Create a bundle with no track.
    br = clarify.create_bundle(name='track tester')
    href = br['_links']['clarify:tracks']['href']

    # Add three tracks.
    r = clarify.create_track(href,
                               media_url=MEDIA_URL1, label='first label')
    r = clarify.create_track(href,
                               media_url=MEDIA_URL2, label='second label')
    r = clarify.create_track(href,
                               media_url=MEDIA_URL3, label='third label')
                       
    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

    print '*** Deleting all tracks...'

    # Update the track.
    r = clarify.delete_track(href)

    # List the tracks.
    tl = clarify.get_track_list(br['_links']['clarify:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

def print_track(track):

    print '** Track ' + str(track['track'])
    if track.has_key('label'):
        print 'label: ' + track['label']
    print 'media_url: ' + track['media_url']
    print 'created: ' + track['created']
    print 'updated: ' + track['updated']
    print 'status: ' + track['status']
    if track.has_key('mime_type'):
        print 'mime_type: ' + track['mime_type']
    print 'size: ' + str(track['size'])
    print 'duration: ' + str(track['duration'])

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    delete_1_track()
    delete_all_tracks()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
