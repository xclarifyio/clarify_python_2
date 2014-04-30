##
##  This file contains all bundle class definitions.  Objects of these
##  Classes can be instantiated by passing them the data structures
##  returned by the audio and video library functions.
##

import datetime
import collections
import op3nvoice

KEY_LINKS = '_links'
KEY_EMBEDDED = '_embedded'
KEY_HREF = 'href'
KEY_TOTAL = 'total'
KEY_ID = 'id'
KEY_BUNDLE_ID = 'bundle_id'
KEY_VERSION = 'version'
KEY_NAME = 'name'
KEY_STATUS = 'status'
KEY_NOTIFY_URL = 'notify_url'
KEY_CREATED = 'created'
KEY_UPDATED = 'updated'
KEY_DATA = 'data'
KEY_METADATA = 'o3v:metadata'
KEY_TRACKS = 'o3v:tracks'
KEY_TRACK_LIST = 'tracks'
KEY_TRACK_NUMBER = 'track'
KEY_LABEL = 'label'
KEY_MEDIA_URL = 'media_url'
KEY_AUDIO_CHANNEL = 'audio_channel'
KEY_SOURCE = 'source'
KEY_STATUS = 'status'
KEY_MIME_TYPE = 'mime_type'
KEY_SIZE = 'size'
KEY_DURATION = 'duration'

REL_PARENT = 'parent'
REL_SELF = 'self'
REL_FIRST = 'first'
REL_LAST = 'last'
REL_PREVIOUS = 'previous'
REL_NEXT = 'next'
REL_ITEMS = 'items'
REL_METADATA = 'o3v:metadata'
REL_TRACKS = 'o3v:tracks'

EMBEDDED_ITEMS = 'items'
EMBEDDED_METADATA = 'o3v:metadata'
EMBEDDED_TRACKS = 'o3v:tracks'

AUDIO_CHANNEL_BOTH = ''
AUDIO_CHANNEL_LEFT = 'left'
AUDIO_CHANNEL_RIGHT = 'right'

AUDIO_SOURCE_PHONE = 'phone'
AUDIO_SOURCE_GENERIC = ''

AUDIO_STATUS_READY = 'ready'
AUDIO_STATUS_QUEUED = 'queued'
AUDIO_STATUS_PROCESSING = 'processing'
AUDIO_STATUS_ERROR = 'error'

class BundleList(object):

    _data_struct = None

    def __init__(self, ds):
        """The only initializer you should use.

        'ds' is a python data structure that should not be null."""

        # Argument error checking.
        assert ds != None
        
        self._data_struct = ds

    def get_bundle_hrefs(self):
        """Returns a list of URLs to all the bundles in this page, never
        None."""

        result = []

        links = self._data_struct[KEY_LINKS]
        for i in links[REL_ITEMS]:
            result.append(i[KEY_HREF])

        return result

    def has_previous_href(self):
        """Returns True if there are more bundles available on
        a previous page."""

        result = False

        links = self._data_struct[KEY_LINKS]
        if links.has_key(REL_PREVIOUS):
            result = True

        return result

    def has_next_href(self):
        """Returns True if there are more bundles available on
        an earlier page."""

        result = False

        links = self._data_struct[KEY_LINKS]
        if links.has_key(REL_NEXT):
            result = True

        return result

    def get_previous_href(self):
        """Returns the URL for the previous page of bundles, or None
        if there is no such page."""

        result = None

        links = self._data_struct[KEY_LINKS]
        if links.has_key(REL_PREVIOUS):
            result = links[REL_PREVIOUS][KEY_HREF]

        return result

    def get_next_href(self):
        """Returns the URL for the next page of bundles, or None
        if there is no such page."""

        result = None

        links = self._data_struct[KEY_LINKS]
        if links.has_key(REL_NEXT):
            result = links[REL_NEXT][KEY_HREF]

        return result

    def get_first_href(self):
        """Returns the URL for he first page of bundles, never None."""

        result = None

        links = self._data_struct[KEY_LINKS]
        result = links[REL_FIRST][KEY_HREF]

        return result

    def get_last_href(self):
        """Returns the URL for he last page of bundles, never None."""

        result = None

        links = self._data_struct[KEY_LINKS]
        result = links[REL_LAST][KEY_HREF]
        
        return result

    def get_total(self):
        """Returns the total number of bundles available, never None."""

        result = self._data_struct[KEY_TOTAL]

        return result

    def has_bundles(self):
        """Returns True if contains embedded bundles."""

        return self._data_struct.has_key(KEY_EMBEDDED)

    def get_bundles(self):
        """Returns a list of bundle data structure equivalent to the
        JSON returned by the API.  Each element in the list can be used
        to instantiate a Bundle.

        If no bundles are available, returns None."""

        result = None

        if self.has_bundles():
            result = self._data_struct[KEY_EMBEDDED][EMBEDDED_ITEMS]

        return result

class Reference(object):

    _data_struct = None

    def __init__(self, ds):
        """The only initializer you should use.

        'ds' is a python data structure that should not be null."""

        # Argument error checking.
        assert ds != None
        
        self._data_struct = ds

    def has_rel(self, name):
        """Returns True if the link relationship exists, False
        otherwise.

        'name' the name of the link relationship.  May not be None."""

        assert name != None

        result = False

        links = self._data_struct[KEY_LINKS]
        if links.has_key(name):
            result = True

        return result
    
    def get_rel(self, name):
        """Returns the href of the link relationship, or None, if
        it doesn't exist.

        'name' the name of the link relationship.  May not be None."""

        assert name != None

        result = None

        links = self._data_struct[KEY_LINKS]
        rel = links.get(name)

        if rel != None:
            result = rel[KEY_HREF]

        return result

    def get_parent_href(self):
        """Returns the URL to the parent data structure. May be None."""

        return self.get_rel(REL_PARENT)


    def get_self_href(self):
        """Returns the URL to the current data structure, never None."""

        return self.get_rel(REL_SELF)


class BundleReference(Reference):

    _data_struct = None

    def __init__(self, ds):
        """The only initializer you should use.

        'ds' is a python data structure that should not be null."""

        Reference.__init__(self, ds)
        
    def get_id(self):
        """Returns the new bundle ID, never None."""

        return self._data_struct[KEY_ID]

    def get_metadata_href(self):
        """Returns the URL to the metadata. This URL will exist even
        if the bundle currently has no metadata."""

        return self.get_rel(REL_METADATA)

    def get_track_list_href(self):
        """Returns the URL to the media track list. This URL will exist
        even if the bundle currently has no media tracks."""

        return self.get_rel(REL_TRACKS)


class Bundle(BundleReference):

    _data_struct = None

    def __init__(self, ds):
        """The only initializer you should use.

        'ds' is a python data structure that should not be null."""

        BundleReference.__init__(self, ds)

    def get_version(self):
        """Returns the object version, never None."""

        return self._data_struct[KEY_VERSION]

    def get_name(self):
        """Returns the name given to the bundle, or None if no name
        exists."""

        # Note that the JSON we get back from API currently always
        # contains a 'name' field, but checking in case that changes.

        result = None

        name = self._data_struct.get(KEY_NAME)
        if name != None and name != "":
            result = name
        
        return result

    def has_notify_url(self):
        """Returns True if a notify URL has been set, False otherwise."""

        return self._data_struct.has_key(KEY_NOTIFY_URL)

    def get_notify_url(self):
        """Returns the URL to which notifications about this bundle will
        be sent, or none if no URL was specified."""

        # Note that the JSON we get back from API currently only 
        # contains a 'notify_url' field when the URL has been set, but
        # checking for empty string in case that changes.

        result = None

        notify_url = self._data_struct.get(KEY_NOTIFY_URL)
        if notify_url != None and notify_url != "":
            result = notify_url

        return result

    def get_created(self):
        """Returns the date and time the bundle was created as an ISO
        8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utility function
        datetime_from_string()."""

        return self._data_struct[KEY_CREATED]

    def get_updated(self):
        """Returns the date and time the bundle was last update as an
        ISO 8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utility function
        datetime_from_string()."""

        return self._data_struct[KEY_UPDATED]

    def has_metadata(self):
        """Returns True if we have metadata available, False otherwise."""

        result = False

        if self._data_struct.has_key(KEY_EMBEDDED):
            embedded = self._data_struct[KEY_EMBEDDED]
            if embedded.has_key(KEY_METADATA):
                result = True

        return result

    def has_tracks(self):
        """Returns True if we have tracks available, False otherwise."""

        result = False

        if self._data_struct.has_key(KEY_EMBEDDED):
            embedded = self._data_struct[KEY_EMBEDDED]
            if embedded.has_key(KEY_TRACKS):
                result = True

        return result

    def get_metadata(self):
        """Returns a data structure equivalent to the JSON returned by
        the API.  This data structure can be used to instantiate a
        Metadata. Returns None if no embedded metadata is available."""

        result = None

        if self.has_metadata():
             result = self._data_struct[KEY_EMBEDDED][KEY_METADATA]

        return result

    def get_tracks(self):
        """Returns a data structure equivalent to the JSON returned by
        the API.  This data structure can be used to instantiate a
        TrackList.  Returns None if no embedded tracks are available."""

        result = None

        if self.has_tracks():
            result = self._data_struct[KEY_EMBEDDED][KEY_TRACKS]

class Metadata(Reference):

    _data_struct = None

    def __init__(self, ds):
        """The only initializer you should use.

        'ds' is a python data structure that should not be null."""

        Reference.__init__(self, ds)
        
    def get_bundle_id(self):
        """Returns the ID of the parent bundle, never None."""

        return self._data_struct[KEY_BUNDLE_ID]

    def get_version(self):
        """Returns the object version, never None."""

        return self._data_struct[KEY_VERSION]

    def get_created(self):
        """Returns the date and time the metadata was created as an ISO
        8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utility function
        datetime_from_string()."""

        return self._data_struct[KEY_CREATED]

    def get_updated(self):
        """Returns the date and time the metadata was last update as an
        ISO 8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utility function
        datetime_from_string()."""

        return self._data_struct[KEY_UPDATED]

    def has_data(self):
        """Returns True if metadata data is available."""

        # Implementation note.
        #
        # When there's no data the API returns: "data": {}
        # This fuction treats that as None.

        result = True

        d = self._data_struct[KEY_DATA]
        if d == {}:
            result = False

        return result

    def get_data(self):
        """Returns a dictionary of metadata, or None if none exists."""

        return self._data_struct.get(KEY_DATA)

class TrackList(Reference):

    _data_struct = None

    def __init__(self, ds):
        """The only initializer you should use.

        'ds' is a python data structure that should not be null."""

        Reference.__init__(self, ds)
        
    def get_bundle_id(self):
        """Returns the ID of the parent bundle, never None."""

        return self._data_struct[KEY_BUNDLE_ID]

    def get_version(self):
        """Returns the object version, never None."""

        return self._data_struct[KEY_VERSION]

    def get_created(self):
        """Returns the date and time the metadata was created as an ISO
        8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utility function
        datetime_from_string()."""

        return self._data_struct[KEY_CREATED]

    def get_updated(self):
        """Returns the date and time the metadata was last update as an
        ISO 8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utilty function
        datetime_from_string()."""

        return self._data_struct[KEY_UPDATED]

    def get_count(self):
        """Returns the number of tracks available."""

        return len(self._data_struct[KEY_TRACK_LIST])

    def get_track(self, index):
        """Returns a data structure equivalent to the JSON returned by
        the API.  This data structure can be used to instantiate a
        Track.  If index is out of range, returns None. 

        'index' must be >= 0."""

        assert index >= 0

        result = None

        # Putting this into a try/except to allow the operation
        # to be atomic.
        try: 
            result = self._data_struct[KEY_TRACK_LIST][index]
        except IndexError:
            pass

        return result

    def get_total(self):
        """Returns the number of tracks available."""

        return len(self._data_struct[KEY_TRACK_LIST])

class Track(object):

    _data_struct = None

    def __init__(self, ds):
        """The only initializer you should use.

        'ds' is a python data structure that should not be null."""

        # Argument error checking.
        assert ds != None
        
        self._data_struct = ds

    def get_track_number(self):
        """Returns the track number, which is also the index in the
        array of tracks.  Never None."""

        return self._data_struct[KEY_TRACK_NUMBER]

    def get_label(self):
        """Returns a track label, or None."""

        result = None

        label = self._data_struct[KEY_LABEL]
        if label != None and label != '': # Checking for None in case 
            result = label                # things change.

        return result
        
    def get_media_url(self):
        """Returns the URL from which the media was originally fetched.
        Never None."""

        return self._data_struct[KEY_MEDIA_URL]

    def get_audio_channel(self):
        """Returns which of the media's audio channels was use. Possible
        values are: AUDIO_CHANNEL_LEFT, AUDIO_CHANNEL_RIGHT, and
        AUDIO_CHANNEL_BOTH. Never None."""

        return self._data_struct[KEY_AUDIO_CHANNEL]

    def get_source(self):
        """Returns the source of the recording. Possible values are:
        AUDIO_SOURCE_PHONE and AUDIO_SOURCE_GENERIC. Never None."""

        return self._data_struct[KEY_SOURCE]

    def get_language(self):
        """Returns the language of the recording. Implementation is
        still undocumented. This is a placeholder.  TODO."""
        pass

    def get_created(self):
        """Returns the date and time the metadata was created as an ISO
        8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utility function
        datetime_from_string()."""

        return self._data_struct[KEY_CREATED]

    def get_updated(self):
        """Returns the date and time the metadata was last update as an
        ISO 8601 compliant string. To convert this string to a datetime
        object that is timezone aware, use the utility function
        datetime_from_string()."""

        return self._data_struct[KEY_UPDATED]

    def get_status(self):
        """Returns the processing status of the track. Possible values
        are: AUDIO_STATUS_READY, AUDIO_STATUS_QUEUED, and
        AUDIO_STATUS_PROCESSING, AUDIO_STATUS_ERROR. Never None."""

        return self._data_struct[KEY_STATUS]

    def get_mime_type(self):
        """Returns the media type.  May be None if the type couldn't be
        determined."""

        result = None

        mime_type = self._data_struct[KEY_MIME_TYPE]
        if mime_type != None and mime_type != '': # Checking for None in 
            result = mime_type                    # case things change.

        return result

    def get_size(self):
        """Returns the number of bytes in the media, a positive integer."""

        return self._data_struct[KEY_SIZE]

    def get_duration(self):
        """Returns the number of seconds in the media, a positive integer."""

        return self._data_struct[KEY_DURATION]

        
class UTC(datetime.tzinfo):

    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return datetime.timedelta(0)

def datetime_from_string(timestring):
    """We know that our date strings are ISO 8601, and we know that they
    will always have Z as a timezeone.  Since the datetime library
    doesn't deal with timezones properly, we'll strip off the Z and set
    the timezone of the datetime object to UTC manually."""

    s = timestring[:-1]
    result = datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f')
    result = result.replace(tzinfo=UTC())

    return result
    
