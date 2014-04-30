#!/usr/bin/python

##
##  Some test functions used to sanity check during development. Not
##  unit tests.
##

import sys
sys.path.append('..')
from op3nvoice_python_2 import op3nvoice
from op3nvoice_python_2 import op3nvoice_plus

ak = None # our app key.

MEDIA_URL1 = 'http://www.kqed.org/.stream/anon/radio/hd/2008/09/2008-09-18c-hd.mp3'
MEDIA_URL2 = 'http://feedproxy.google.com/~r/kqed/ClimateWatch/~5/UTaeFBdvZSw/2012-05-04a-tcr.mp3'

def set_appkey(key):
    global ak
    ak = key

def track_update():
    c = op3nvoice.Connection(ak)

    print '*** Creating a bundle with no tracks...'

    # Create a bundle with no track.
    _br = op3nvoice.create_bundle(c, name='track tester')
    br = op3nvoice_plus.BundleReference(_br)

    # List the tracks.
    _tl = op3nvoice.get_track_list(c, br.get_track_list_href())
    tl = op3nvoice_plus.TrackList(_tl)
    for i in range(0, tl.get_count()):
        _t = tl.get_track(i)
        print_track(op3nvoice_plus.Track(_t))

    print '*** Adding a track to the bundle...'

    # Add a track.
    _r = op3nvoice.create_track(c, br.get_track_list_href(),
                                media_url=MEDIA_URL1, label='first label')
                       
    # List the tracks.
    _tl = op3nvoice.get_track_list(c, br.get_track_list_href())
    tl = op3nvoice_plus.TrackList(_tl)
    for i in range(0, tl.get_count()):
        _t = tl.get_track(i)
        print_track(op3nvoice_plus.Track(_t))

    print '*** Changing the track...'

    # Update the track.
    _r = op3nvoice.update_track(c, br.get_track_list_href(), track=0,
                                media_url=MEDIA_URL2, label='second label')

    # List the tracks.
    _tl = op3nvoice.get_track_list(c, br.get_track_list_href())
    tl = op3nvoice_plus.TrackList(_tl)
    for i in range(0, tl.get_count()):
        _t = tl.get_track(i)
        print_track(op3nvoice_plus.Track(_t))
    

def print_track(track):

    print '** Track ' + str(track.get_track_number())
    label = track.get_label()
    if label != None:
        print 'label: ' + label
    print 'media_url: ' + track.get_media_url()
    source = track.get_source()
    print 'source: ' + source + '(NB: an empty source means generic.)'
    print 'update: ' + track.get_updated()
    print 'status: ' + track.get_status()
    mime_type = track.get_mime_type()
    if mime_type != None:
        print 'mime_type: ' + mime_type
    print 'size: ' + str(track.get_size())
    print 'duration: ' + str(track.get_duration())

def all(_ak=None):
    if _ak != None:
        set_appkey(_ak)
    
    track_update()
    
if __name__ == '__main__':

    set_appkey(sys.argv[1])

    all()
