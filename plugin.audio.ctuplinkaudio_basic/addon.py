#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# c't uplink - The Audio Podcast Kodi Plug-in
# by Achim Barczok, Heise Medien
#
# Diese Basisversion entspricht dem Beispiel in c't 19/2018
# eine etwas schönere und umfangreiche Version 
# finden Sie unter plugin.audio.ctuplinkaudio

import sys
import xbmcgui
import xbmcplugin
import feedparser

#Selbst-Referenzierung fürs Plug-in
addon_handle = int(sys.argv[1])

#Siedle Plug-in in den Bereich Audio
xbmcplugin.setContent(addon_handle, 'audio')


#Parse ctuplink-Feed
d = feedparser.parse('https://www.heise.de/ct/uplink/ctuplink.rss')

for item in d['entries']:
    title = item['title']
    url = item.enclosures[0].href
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=xbmcgui.ListItem(title))

#Schließe die Liste ab
xbmcplugin.endOfDirectory(addon_handle, succeeded=True)