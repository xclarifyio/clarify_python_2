##
##  Functions used by multiple tests.
##

import sys
sys.path.append('..')
from op3nvoice_python_2 import op3nvoice

def bundle_list_map(func, connection):
    """Execute func on every bundle."""
    has_next = True
    next_href = None # if None, retrieves first page

    while has_next:
        # Get a page and perform the requested function.
        bl = op3nvoice.get_bundle_list(connection, next_href)
        for i in bl['_links']['items']:
            href = i['href']
            func(connection, href)
        # Check for following page.
        next_href = None
        if bl['_links'].has_key('next'):
            next_href = bl['_links']['next']['href']
        if next_href == None:
                has_next = False
