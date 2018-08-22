#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# c't uplink - The Video Podcast Kodi Plug-in
# by Achim Barczok, Heise Medien
#


import xbmc
#Öffne den Youtube-Channel von c't uplink im Playlist-Fenster des Youtube-Plug-ins

if __name__ == '__main__':
    xbmc.executebuiltin("ActivateWindow(10028,)")
    xbmc.executebuiltin("Container.Update(plugin://plugin.video.youtube/play/?playlist_id=PLUoWfXKEShjdcawz_wBJVqkv0pVIakmSP&order=default)")	
