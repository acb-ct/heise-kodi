#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# heiseshow - The Video Podcast Kodi Plug-in
# by Achim Barczok, Heise Medien
#


import xbmc
#Mit dem Youtube-Plugin die heiseshow Playlist abspielen, sobald die App geöffnet wird (__main__)
#Zuerst das Window 10028 aktivieren (Playlist-Bereich im Youtube-Plugin)
#Dann den aktivierten Container mit der Playlist heiseshow aktualisieren
if __name__ == '__main__':
    xbmc.executebuiltin("ActivateWindow(10028,)")
    xbmc.executebuiltin("Container.Update(plugin://plugin.video.youtube/play/?playlist_id=PLUoWfXKEShjeEJJ83lJkme2DKyFUrDBpz&order=default)")	