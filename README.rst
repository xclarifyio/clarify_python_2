===============================
Clarify Python 2 Helper Library
===============================

Python 2.x helper library for the Clarify API

* Free software: MIT license

Installing
----------

.. code-block:: bash

   $ pip install clarify_python_2

You may need to use sudo if you don't have permission to install.

Upgrading
---------

If you are running an older version of the python helper library, please upgrade.

.. code-block:: bash

   $ pip install --upgrade clarify_python_2

You may need to use sudo if you don't have permission to upgrade.

Quickstart Guide
----------------

Getting Started
^^^^^^^^^^^^^^^

This quickstart demonstrates a simple way to get started using the Clarify API. Following these steps, it should take you no more than 5-10 minutes to have a fully functional search for your audio.

Configuring Your Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While you can use any programming language you choose, we provide helping libraries in a few to get you started.  In Python, you simply include the Clarify file from the python_2 module, and initialize the environment with your API key:

.. code-block:: python

	from clarify_python_2 import clarify

	clarify.set_key('my api key')

Loading Audio
^^^^^^^^^^^^^

Once you've initialied the environment with your API key, you load a file like this:

.. code-block:: python

	clarify.create_bundle(name='test bundle', media_url='http://example.com/sample-audio-file.wav')

Naming the bundle is optional.  

Here are some audio files you can use for testing:

::

	http://media.clarify.io/audio/samples/harvard-sentences-1.wav
	http://media.clarify.io/audio/samples/harvard-sentences-2.wav
	http://media.clarify.io/audio/books/dorothyandthewizardinoz_01_baum_64kb.mp3

Hint: You don't have to download these files. Instead you can pass us these urls via the create_bundle() method shown above.
	
Searching Audio
^^^^^^^^^^^^^^^

To search, we'll use the search() function. If you uploaded the *Wizard of Oz* audio clip, you can search for "dorothy":

.. code-block:: python

	clarify.search(query='dorothy')

Then you can process and interact the results however you wish. The code below simply shows the resulting bundle id, bundle name, and the start/end offsets for each occurrence of the search terms. This assumes that the audio clip has been indexed by the time you search. If it hasn't, wait and try again in a few minutes.

.. code-block:: python

	result = clarify.search(query='dorothy')
	results = result['item_results']
	items = result['_links']['items']

	index = 0
	for item in items:
	    bundle = clarify.get_bundle(item['href'])

	    print bundle['name']

    	    search_hits = results[index]['term_results'][0]['matches'][0]['hits']
    	    for search_hit in search_hits:
            	print str(search_hit['start']) + ' -- ' + str(search_hit['end'])

    	    ++index
	
And here are the results using the *Wizard of Oz* clip we loaded.

::

	dorothy and her friends
	2.35 -- 2.59
	172.49 -- 172.83
	224.82 -- 225.08
	271.49 -- 271.8
	329.1 -- 329.31
	480.45 -- 480.92

Putting it all Together
^^^^^^^^^^^^^^^^^^^^^^^

From here, we can visualize our search results with the included audio player.  The player should work with no additional configuration, but the bulk of the logic is here:

.. code-block:: python

	import json

	result = clarify.search(query='dorothy')
	search_terms = json.dumps(result['search_terms'])
	item_results = json.dumps(result['item_results'])

	bundleref = result['_links']['items'][0]['href']
	bundle = clarify.get_bundle(bundleref)
	tracksref = bundle['_links']['clarify:tracks']['href']
	tracks = clarify.get_track_list(tracksref)['tracks']
	mediaURL = tracks[0]['media_url']


History (Change Log)
--------------------

See `HISTORY.rst <HISTORY.rst>`_

TODO
----

See `TODO.rst <TODO.rst>`_

