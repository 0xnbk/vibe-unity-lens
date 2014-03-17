import urllib2
import simplejson

import logging
import optparse

import gettext
from gettext import gettext as _
gettext.textdomain('vibe')

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from vibe import vibeconfig

class VibeLens(SingleScopeLens):
    vibe = "https://vibeapp.co/api/v1"

    class Meta:
        name = 'vibe'
        description = 'Vibe Lens'
        search_hint = 'Search Email'
        icon = 'vibe.svg'
        search_on_blank=True

    # TODO: Add your categories
    user_category = ListViewCategory("Examples", 'help')

    def vibe_query(self,search):
        try:
            search = search.replace(" ", "|")
            url = ("%s/initial_data/?api_key=526541b013ef526c04c211a45a2fc6ec&email=%s&platform=chrome" % (self.vibe, search))
            results = simplejson.loads(urllib2.urlopen(url).read())
            print "Searching Vibe"
            return results[1]
        except (IOError, KeyError, urllib2.URLError, urllib2.HTTPError, simplejson.JSONDecodeError):
            print "Error : Unable to search Vibe"
            return []

    def search(self, search, results):
        for info in self.vibe_query(search):
            print info
            results.append(info.websites,
                        info.profile_picture,
                        self.user_category,
                        "text/html",
                        info.name,
                        info.bio,
                        info.websites)
    pass
