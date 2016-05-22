# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:18:28 2016

@author: Annakoppad
"""

import urllib2 
url="http://facebook.com/annakoppad"
page=urllib2.urlopen(url)
for a in page:
    print a