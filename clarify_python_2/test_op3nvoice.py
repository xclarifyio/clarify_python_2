""" Sample test file. """

import os
from clarify_python_2 import clarify

KEY_SET = False


def set_key():
    """NB: This should really be an initialization function."""

    global KEY_SET

    if KEY_SET is False:
        api_key = os.environ['API_KEY']
        clarify.set_key(api_key)
        KEY_SET = True


def test_bundle_list():
    """Make sure we can get a list of bundles."""

    set_key()
    assert clarify.get_bundle_list() is not None
