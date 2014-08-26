.. :changelog:

History
-------

1.0.0 (2014-08-26)
++++++++++++++++++

* Updated to the 1.0 API.
* NB: The semantics of delete_track() have changed. delete_track() now takes an href to a track. To delte a track by index you now need to call delete_track_at_index().

0.9.0 (2014-06-16)
++++++++++++++++++

* Removed 'source' attribute from bundle.

0.8.0 (2014-05-04)
++++++++++++++++++

* Simplified initialization (and removed threading restriction).
* Separated REST cover and object libraries.
* Moved configuration variables into module's __init__.py file.

0.7.0 (2014-04-30)
++++++++++++++++++

* New repo name.

0.3.0 (2014-04-26)
++++++++++++++++++

* Code cleanup.
* get_bundle_href() changed to get_self_href().
* Switched to new style classes.

0.1.0 (2014-04-20)
++++++++++++++++++

* First release.

