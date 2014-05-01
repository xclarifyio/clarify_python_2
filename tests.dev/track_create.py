#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from op3nvoice_python_2 import op3nvoice

ak = None # our app key.

MEDIA_URL1 = 'http://www.kqed.org/.stream/anon/radio/hd/2008/09/2008-09-18c-hd.mp3'
MEDIA_URL2 = 'http://feedproxy.google.com/~r/kqed/ClimateWatch/~5/UTaeFBdvZSw/2012-05-04a-tcr.mp3'

def set_appkey(key):
    global ak
    ak = key

def track_create_and_list():
    c = op3nvoice.Connection(ak)

    print '*** Creating a bundle with a track...'

    # Create a bundle with a track.
    br = op3nvoice.create_bundle(c, name='track tester', media_url=MEDIA_URL1)

    # List the tracks.
    tl = op3nvoice.get_track_list(c, br['_links']['o3v:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

    print '*** Adding a track to the bundle...'

    # Add a track.
    r = op3nvoice.create_track(c, br['_links']['o3v:tracks']['href'],
                               media_url=MEDIA_URL2)
                       
    # List the tracks.
    tl = op3nvoice.get_track_list(c, br['_links']['o3v:tracks']['href'])
    for i in tl['tracks']:
        print_track(i)

def print_track(track):

    print '** Track ' + str(track['track'])
    if track.has_key('label'):
        print 'label: ' + track['label']
    print 'media_url: ' + track['media_url']
    source = track['source']
    print 'source: ' + source + '(NB: an empty source means generic.)'
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
    
    track_create_and_list()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
