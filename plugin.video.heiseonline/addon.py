#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# heise online - The Video Podcast Kodi Plug-in
# by Achim Barczok, Heise Medien
#

import xbmc
#Öffne den Youtube-Kanal von heise online im Video-Fenster
if __name__ == '__main__':
   xbmc.executebuiltin("ActivateWindow(10025,plugin://plugin.video.youtube/user/heisenewsticker/)")
