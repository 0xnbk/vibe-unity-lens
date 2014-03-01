import logging
import optparse

import gettext
from gettext import gettext as _
gettext.textdomain('vibe')

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from vibe import vibeconfig

class VibeLens(SingleScopeLens):

    class Meta:
        name = 'vibe'
        description = 'Vibe Lens'
        search_hint = 'Search Vibe'
        icon = 'vibe.svg'
        search_on_blank=True

    # TODO: Add your categories
    example_category = ListViewCategory("Examples", 'help')

    def search(self, search, results):
        # TODO: Add your search results
        results.append('https://wiki.ubuntu.com/Unity/Lenses/Singlet',
                         'ubuntu-logo',
                         self.example_category,
                         "text/html",
                         'Learn More',
                         'Find out how to write your Unity Lens',
                         'https://wiki.ubuntu.com/Unity/Lenses/Singlet')
        pass
