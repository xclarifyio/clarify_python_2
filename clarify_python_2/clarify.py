##
##  This file contains all of the functions covering the REST API calls.
##  These calls (except for delete_* which are void) all return a python
##  data structure equivalent to the JSON returned by the API.
##

import sys
import urllib
import httplib
import collections
import json
import urlparse
from __init__ import __version__
from __init__ import __api_version__
from __init__ import __api_lib_name__
from __init__ import __host__
from __init__ import __debug_level__

BUNDLES_PATH = 'bundles'
SEARCH_PATH = 'search'
PYTHON_VERSION = '.'.join(map(str, sys.version_info[:3]))

_key = None

###
###  The API functions.
###

def get_bundle_list(href=None, limit=None, embed_items=None,
                    embed_tracks=None, embed_metadata=None):
    """Get a list of available bundles.

    'href' the relative href to the bundle list to retriev. If None, the
    first bundle list will be returned.
    'limit' the maximum number of bundles to include in the
    result. 
    'embed_items' whether or not to expand the bundle data into the result.
    'embed_tracks' whether or not to expand the bundle track data into
    the result.
    'embed_metadata' whether or not to expand the bundle metadata into
    the result.

    NB: providing values for 'limit', 'embed_*' will override either the
    API default or the values in the provided href.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a BundleList.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""

    # Argument error checking.
    assert limit == None or limit > 0

    if href == None:
        j = _get_first_bundle_list(limit, embed_items, embed_tracks,
                                   embed_metadata)
    else:
        j = _get_additional_bundle_list(href, limit, embed_items,
                                        embed_tracks, embed_metadata)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(j)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, j, msg)

    return result

def _get_first_bundle_list(limit=None, embed_items=None,
                           embed_tracks=None, embed_metadata=None):
    """Get a list of available bundles.

    'limit' may be None, which implies API default.  If not None, must be > 1.
    'embed_items' True will embed item data in the result.
    'embed_tracks' True will embed track data in the embeded items.
    'embed_metadata' True will embed metadata in the embeded items.

    Note that including tracks and metadata without including items is
    meaningless.  
    
    Returns the raw JSON returned by the API.

    If the response status is not 2xx, throws an APIException."""

    # Prepare the data we're going to include in our query.
    path = '/' + __api_version__ + '/' + BUNDLES_PATH
    
    data = None
    fields = {}
    if limit != None:
        fields['limit'] = limit
    embed = process_embed(embed_items=embed_items,
                          embed_tracks=embed_tracks,
                          embed_metadata=embed_metadata)
    if embed != None:
        fields['embed'] = embed

    if len(fields) > 0:
        data = fields
    
    raw_result = get(path, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)
    else:
        result = raw_result.json

    return result

def _get_additional_bundle_list(href=None, limit=None, embed_items=None,
                                embed_tracks=None, embed_metadata=None):
    """Get next, previous, first, last list (page) of available bundles.

    'href' the href to retrieve the bundles.

    All other arguments override arguments in the href.

    Returns the raw JSON returned by the API.

    If the response status is not 2xx, throws an APIException."""

    url_components = urlparse.urlparse(href)
    path = url_components.path
    data = urlparse.parse_qs(url_components.query)

    # Deal with limit overriding.
    if limit != None:
        data['limit'] = limit

    # Deal with embeds overriding.
    href_embed = None
    if data.has_key('embed'):
        href_embed = data['embed'][0] # parse_qs puts values in a list.
    final_embed = process_embed_override(href_embed,
                                         embed_items,
                                         embed_tracks,
                                         embed_metadata)
    if final_embed != None:
        data['embed'] = final_embed

    raw_result = get(path, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)
    else:
        result = raw_result.json

    return result

def create_bundle(name=None, media_url=None, audio_channel=None,
                  metadata=None, notify_url=None):
                  
    """Create a new bundle. 

    'metadata' may be None, or an object that can be converted to a JSON
    string.  See API documentation for restrictions.  The conversion
    will take place before the API call.

    All other parameters are also optional. For information about these
    see https://api.clarify.io/docs#!/audio/v1audio_post_1.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a BundleReference.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""

    # Prepare the data we're going to include in our bundle creation.
    path = '/' + __api_version__ + '/' + BUNDLES_PATH

    data = None

    fields = {}
    if name != None:
        fields['name'] = name
    if media_url != None:
        fields['media_url'] = media_url
    if audio_channel != None:
        fields['audio_channel'] = audio_channel
    if metadata != None:
        fields['metadata'] = json.dumps(metadata)
    if notify_url != None:
        fields['notify_url'] = notify_url
        
    if len(fields) > 0:
        data = fields

    raw_result = post(path, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(raw_result.json)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, raw_result.json, msg)

    return result
    
def delete_bundle(href=None):
    """Delete a bundle.

    'href' the relative href to the bundle. May not be None.

    Returns nothing.

    If the response status is not 204, throws an APIException."""

    # Argument error checking.
    assert href != None

    raw_result = delete(href)

    if raw_result.status != 204:
        raise APIException(raw_result.status, raw_result.json)

def get_bundle(href=None, embed_tracks=False, embed_metadata=False):
    """Get a bundle.

    'href' the relative href to the bundle. May not be None.
    'embed_tracks' determines whether or not to include track
    information in the response.
    'embed_metadata' determines whether or not to include metadata
    information in the response.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a Bundle.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""

    # Argument error checking.
    assert href != None

    data = None
    fields = {}
    embed = process_embed(embed_items=False,
                          embed_tracks=embed_tracks,
                          embed_metadata=embed_metadata)
    if embed != None:
        fields['embed'] = embed

    if len(fields) > 0:
        data = fields

    raw_result = get(href, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(raw_result.json)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, raw_result.json, msg)

    return result

def update_bundle(href=None, name=None, notify_url=None, version=None):
    """Update a bundle.  Note that only the 'name' and 'notify_url' can
    be update.

    'href' the relative href to the bundle. May not be None.
    'name' the name of the bundle.  May be None.
    'notify_url' the URL for notifications on this bundle.
    'version' the object version.  May be None; if not None, must be
    an integer, and the version must match the version of the bundle.  If
    not, a 409 conflict error will cause an APIException to be thrown.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a Reference.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""

    
    # Argument error checking.
    assert href != None
    assert version == None or isinstance(version, int)

    # Prepare the data we're going to include in our bundle update.
    data = None

    fields = {}
    if name != None:
        fields['name'] = name
    if notify_url != None:
        fields['notify_url'] = notify_url
    if version != None:
        fields['version'] = version

    if len(fields) > 0:
        data = fields

    raw_result = put(href, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(raw_result.json)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, raw_result.json, msg)

    return result

def get_metadata(href=None):
    """Get metadata.

    'href' the relative href to the bundle. May not be None.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a Metadata.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""
    
    # Argument error checking.
    assert href != None

    raw_result = get(href)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(raw_result.json)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, raw_result.json, msg)

    return result

def update_metadata(href=None, metadata=None, version=None):
    """Update the metadata in a bundle.
    be update.

    'href' the relative href to the metadata. May not be None.
    'metadata' may be None, or an object that can be converted to a JSON
    string.  See API documentation for restrictions.  The conversion
    will take place before the API call.
    'version' the object version.  May be None; if not None, must be
    an integer, and the version must match the version of the bundle.  If
    not, a 409 conflict error will cause an APIException to be thrown.
    
    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a Reference.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""

    # Argument error checking.
    assert href != None
    assert metadata != None
    assert version == None or isinstance(version, int)
    
    # Prepare the data we're going to include in our bundle update.
    data = None

    fields = {}
    if version != None:
        fields['version'] = version
    fields['data'] = json.dumps(metadata)

    data = fields 

    raw_result = put(href, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(raw_result.json)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, raw_result.json, msg)

    return result
    
def delete_metadata(href=None):
    """Delete metadata.

    'href' the relative href to the bundle. May not be None.

    Returns nothing.

    If the response status is not 204, throws an APIException."""

    # Argument error checking.
    assert href != None

    raw_result = delete(href)

    if raw_result.status != 204:
        raise APIException(raw_result.status, raw_result.json)

def create_track(href=None, media_url=None, label=None,
                 audio_channel=None):
    """Add a new track to a bundle.  Note that the total number of
    allowable tracks is limited. See the API documentation for details.

    'href' the relative href to the tracks list. May not be None.
    'media_url' public URL to media file. May not be None.
    'label' short name for the track. May be None.
    'audio_channel' the channel(s) to use in a stereo file. May be
    None. For details see the API documentation.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a Reference.

    If the response status is not 2xx, or if the maximum number of
    tracks is exceeded, throws an APIException.  If the JSON to python
    data struct conversion fails, throws an APIDataException."""

    # Argument error checking.
    assert href != None
    assert media_url != None

    # Prepare the data we're going to write.
    data = None

    fields = {}
    fields['media_url'] = media_url
    if label != None:
        fields['label'] = label
    if audio_channel != None:
        fields['audio_channel'] = audio_channel

    if len(fields) > 0:
        data = fields

    raw_result = post(href, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(raw_result.json)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, raw_result.json, msg)

    return result
        
def get_track_list(href=None):
    """Get track list.

    'href' the relative href to the bundle. May not be None.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a TrackList.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""

    # Argument error checking.
    assert href != None

    raw_result = get(href)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(raw_result.json)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, raw_result.json, msg)

    return result

def delete_track(href=None, track=None):
    """Delete a track, or all the tracks.

    'href' the relative href to the bundle. May not be None.
    'track' the index of the track to delete. If none is given,
    all tracks are deleted.
    
    Returns nothing.

    If the response status is not 204, throws an APIException."""

    # Argument error checking.
    assert href != None

    # Deal with any parameters that need to be passed in.
    data = None

    fields = {}
    if track != None:
        fields['track'] = track

    if len(fields) > 0:
        data = fields

    raw_result = delete(href, data)

    if raw_result.status != 204:
        raise APIException(raw_result.status, raw_result.json)

def search(href=None, query=None, query_field=None, filter=None,
           limit=None, embed_items=None, embed_tracks=None,
           embed_metadata=None):
           
    """Search a media collection.

    'href' the relative href to the bundle list to retriev. If None, the
    first bundle list will be returned.
    'query' See API docs for full description. May not be None.
    'query_field' See API docs for full description. May be None.
    'filter' See API docs for full description. May be None.
    'limit' the maximum number of bundles to include in the
    result. 
    'embed_items' whether or not to expand the bundle data into the result.
    'embed_tracks' whether or not to expand the bundle track data into
    the result.
    'embed_metadata' whether or not to expand the bundle metadata into
    the result.

    NB: providing values for 'limit', 'embed_*' will override either the
    API default or the values in the provided href.

    Returns a data structure equivalent to the JSON returned by the API.
    This data structure can be used to instantiate a SearchCollection.

    If the response status is not 2xx, throws an APIException.
    If the JSON to python data struct conversion fails, throws an
    APIDataException."""

    # Argument error checking.
    assert query != None
    assert limit == None or limit > 0
    
    if href == None:
        j = _search_p1(query, query_field, filter, limit, embed_items,
                       embed_tracks, embed_metadata)
                                   
    else:
        j = _search_pn(href, query, query_field, filter, limit,
                       embed_items, embed_tracks, embed_metadata)
                                        

    # Convert the JSON to a python data struct.

    result = None

    try:
        result = json.loads(j)
    except ValueError, e:
        msg = 'Unable to convert JSON string to python data structure.'
        raise APIDataException(e, j, msg)

    return result

def _search_p1(query=None, query_field=None, filter=None, limit=None,
               embed_items=None, embed_tracks=None,
               embed_metadata=None):
    # Prepare the data we're going to include in our query.
    path = '/' + __api_version__ + '/' + SEARCH_PATH
    
    data = None
    fields = {}
    fields['query'] = query
    if query_field != None:
        fields['query_field'] = query_field
    if filter != None:
        fields['filter'] = filter
    if limit != None:
        fields['limit'] = limit
    embed = process_embed(embed_items=embed_items,
                          embed_tracks=embed_tracks,
                          embed_metadata=embed_metadata)
    if embed != None:
        fields['embed'] = embed

    if len(fields) > 0:
        data = fields
    
    raw_result = get(path, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)
    else:
        result = raw_result.json

    return result

def _search_pn(href=None, query=None, query_field=None, filter=None,
               limit=None, embed_items=None, embed_tracks=None,
               embed_metadata=None):
    url_components = urlparse.urlparse(href)
    path = url_components.path
    data = urlparse.parse_qs(url_components.query)


    # Deal with limit overriding.
    if limit != None:
        data['limit'] = limit

    # Deal with embeds overriding.
    href_embed = None
    if data.has_key('embed'):
        href_embed = data['embed'][0] # parse_qs puts values in a list.
    final_embed = process_embed_override(href_embed,
                                         embed_items,
                                         embed_tracks,
                                         embed_metadata)
    if final_embed != None:
        data['embed'] = final_embed

    raw_result = get(path, data)

    if raw_result.status < 200 or raw_result.status > 202:
        raise APIException(raw_result.status, raw_result.json)
    else:
        result = raw_result.json

    return result

###
### Functions to set the API key and perform basic HTTP operations.
###


# This named tuple is returned by get(), put(), post(), delete()
# functions and consumed by the REST cover functions.
Result = collections.namedtuple('Result', ['status', 'json'])

def set_key(key):
    """The API key.  May not be None."""
    global _key
    assert key != None
    _key = key

def _get_headers():
    # So that we can track what library and what version of the
    # helper library people are using and so that we get a
    # sense of what versions of python we need to support.

    if _key == None:
        raise APIConfigurationException('set_key() must be called before any API operations can be performed.')

    user_agent = __api_lib_name__ + '/' + __api_version__ + \
                 '/' + PYTHON_VERSION
        
    return {'Authorization': 'Bearer ' + _key, 
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded'}

def get(path, data=None):
    """Executes a GET.

    'path' may not be None. Should include the full path to the resource.
    'data' may be None or a dictionary. These values will be appended
    to the path as key/value pairs.
        
    Returns a named tuple that includes:
        
    status: the HTTP status code
    json: the returned JSON-HAL

    If the key was not set, throws an APIConfigurationException."""

    # Argument error checking.
    assert path != None
        
    # Open our connection.
    connection = httplib.HTTPSConnection(__host__)
    if __debug_level__ > 0:
        connection.set_debuglevel(__debug_level__)

    # Execute the request.
    fullpath = path
    if data != None:
        fullpath += '?' + urllib.urlencode(data, True)
    connection.request('GET', fullpath, '', _get_headers())
    response = connection.getresponse()

    # Extreact the result.
    s = response.status
    j = response.read()

    # Close our connection.
    connection.close()

    # return (status, json)
    return Result(status=s, json=j)

def post(path, data):
    """Executes a POST.

    'path' may not be None, should not inlude a version number, and
    should not include a leading '/'
    'data' may be None or a dictionary.

    Returns a named tuple that includes:
        
    status: the HTTP status code
    json: the returned JSON-HAL
    
    If the key was not set, throws an APIConfigurationException."""

    # Argument error checking.
    assert path != None
    assert data == None or isinstance(data, dict)
        
    # Open our connection.
    connection = httplib.HTTPSConnection(__host__)
    if __debug_level__ > 0:
        connection.set_debuglevel(__debug_level__)

    # Execute the request.
    encoded_data = ''
    if data != None:
        encoded_data = urllib.urlencode(data, True)
    connection.request('POST', path, encoded_data, _get_headers())
    response = connection.getresponse()

    # Extract the result.
    s = response.status
    j = response.read()

    # Close our connection.
    connection.close()

    # return (status, json)
    return Result(status=s, json=j)

def delete(path, data=None):
    """Executes a DELETE.

    'path' may not be None. Should include the full path to the resoure.
    'data' may be None or a dictionary.

    Returns a named tuple that includes:
        
    status: the HTTP status code
    json: the returned JSON-HAL

    If the key was not set, throws an APIConfigurationException."""    

    # Argument error checking.
    assert path != None
    assert data == None or isinstance(data, dict)

    # Open our connection.
    connection = httplib.HTTPSConnection(__host__)
    if __debug_level__ > 0:
        connection.set_debuglevel(__debug_level__)

    # Execute the request.
    encoded_data = ''
    if data != None:
        encoded_data = urllib.urlencode(data, True)
    connection.request('DELETE', path, encoded_data, _get_headers())
    response = connection.getresponse()

    # Extract the result.
    s = response.status
    j = response.read()

    # Close our connection.
    connection.close()

    # return (status, json)
    return Result(status=s, json=j)
        
def put(path, data):
    """Executes a PUT.

    'path' may not be None. Should include the full path to the resoure.
    'data' may be None or a dictionary.

    Returns a named tuple that includes:
        
    status: the HTTP status code
    json: the returned JSON-HAL

    If the key was not set, throws an APIConfigurationException."""

    # Argument error checking.
    assert path != None
    assert data == None or isinstance(data, dict)
        
    # Open our connection.
    connection = httplib.HTTPSConnection(__host__)
    if __debug_level__ > 0:
        connection.set_debuglevel(__debug_level__)

    # Execute the request.
    encoded_data = ''
    if data != None:
        encoded_data = urllib.urlencode(data, True)
    connection.request('PUT', path, encoded_data, _get_headers())
    response = connection.getresponse()

    # Extract the result.
    s = response.status
    j = response.read()

    # Close our connection.
    connection.close()

    return Result(status=s, json=j)

###
###  Exceptions.
###

KEY_STATUS = 'status'
KEY_MESSAGE = 'message'
KEY_CODE = 'code'

class APIException(Exception):
    """Thown when we don't receive the expected sucess response from an
    API call."""

    _data_struct = None
    http_response = None
    json_response = None

    def __init__(self, http_response, json_response):
        self.http_response = http_response
        self.json_response = json_response

        # That that JSON and turn it into something we can use.
        try:
            self._data_struct = json.loads(json_response)
        except ValueError, e:
            msg = 'Unable to convert JSON string to python data structure.'
            raise APIDataException(e, j, msg)

    def get_http_response(self):
        """Return the HTTP response that caused this exception to be
        thrown."""

        return self.http_response

    def get_status(self):
        """Return the status embedded in the JSON error response body."""

        return self._data_struct[KEY_STATUS]

    def get_message(self):
        """Return the message embedded in the JSON error response body."""

        return self._data_struct[KEY_MESSAGE]

    def get_code(self):
        """Return the code embedded in the JSON error response body. This
        should always match the 'http_response'"""

        return self._data_struct[KEY_CODE]

class APIConfigurationException(Exception):
    """Thrown when the API isn't properly configured."""

    msg = None

    def __init__(self, msg):
        self.msg = msg

    def get_message(self):
        """Returns the error message."""
        return self.msg

class APIDataException(Exception):
    """Thown when we can't parse the data returned by an API call."""

    base_exception = None
    offending_data = None
    msg = None

    def __init__(self, e=Exception, offending_data=None, msg=None):
        """Initializer.

        'msg' is additional information that might be valuable for
        determining the root cause of the exception."""

        self.base_exception = e
        self.offending_data = offending_data
        self.msg = msg

    def get_offending_data(self):
        """Returns the JSON data that caused the exception to be thrown
        in the first place."""

        return self.offending_data

    def get_base_exception(self):
        """Returns the exception that was oritinally thrown and caught
        which in turn generated this one. Unlikely to be useful."""

        return self.base_exception

    def get_msg(self):
        """Return whateve message the application programmer might have
        considered useful when throwing this exception."""

        return self.msg
    
###
###  Utility functions.
###

def process_embed(embed_items=None,
                  embed_tracks=None,
                  embed_metadata=None):
    """Returns an embed field value based on the parameters."""

    result = None
    
    embed = ''
    if embed_items:
        embed = 'items'
    if embed_tracks:
        if embed != '':
            embed += ','
        embed += 'tracks'
    if embed_metadata:
        if embed != '':
            embed += ','
        embed += 'metadata'

    if embed != '':
        result = embed

    return result


def process_embed_override(href_embed=None,
                           embed_items=None,
                           embed_tracks=None,
                           embed_metadata=None):
    """Returns an embed field value based on the parameters."""
    # Our defaults are None, which are the API defaults.
    final_items = None
    final_tracks = None
    final_metadata = None
    
    # First, figure out what was embedded in the original href.
    # If any of the embeds are there, flip the final to True
    if href_embed:
        if 'items' in href_embed:
            final_items = True
        if 'tracks' in href_embed:
            final_tracks = True
        if 'metadata' in href_embed:
            final_metadata = True

    # Second, override the what we have.  
    # None >> Do nothing
    # True >> Set to True
    # False >> Set to None
    if embed_items != None:
        if embed_items == True:
            final_items = True
        else:
            final_items = None
    if embed_tracks != None:
        if embed_tracks == True:
            final_tracks = True
        else:
            final_tracks = None
    if embed_metadata != None:
        if embed_metadata == True:
            final_metadata = True
        else:
            final_metadata = None

    return process_embed(embed_items=final_items, 
                         embed_tracks=final_tracks,
                         embed_metadata=final_metadata)

