# -*- coding: utf-8 -*-
#------------------------------------------------------------
# PT DocS HD
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.pt.docs.hd'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.pt.docs.hd/resources/fan01.png'
iconAA = 'special://home/addons/plugin.video.pt.docs.hd/resources/iconAA.png'
iconAB = 'special://home/addons/plugin.video.pt.docs.hd/resources/iconAB.png'
icon01 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon03.png'
icon04 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon04.png'
icon05 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon05.png'
icon06 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon06.png'
icon07 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon07.png'
icon08 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon08.png'
icon09 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon09.png'
icon10 = 'special://home/addons/plugin.video.pt.docs.hd/resources/icon10.png'





def run():
    plugintools.log("pt.docs.hd.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("pt.docs.hd ===> " + repr(params))
	plugintools.add_item(title = "[ Acredite ou não ]", url = base + "channel/UCunqx90PNIv30uOgn0m4CTg/", thumbnail = iconAA, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Pré-História - Origens ]", url = base + "playlist/PLAg4T2da6qWyDld8XLVstbH4ATeId6d6E/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Civilizações - Impérios ]", url = base + "playlist/PLAg4T2da6qWx4B6j1zPpgbyI-ROEzVeDZ/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Terremotos - Impactos ]", url = base + "playlist/PLAg4T2da6qWz9L4bxdK0jg4d01r50eM6P/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Génios - Teorias ]", url = base + "playlist/PLAg4T2da6qWwvAWWAcD4Pb-6sTrmKiOyf/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Informática - Jogos ]", url = base + "playlist/PLAg4T2da6qWxPRExPKACw5RP3GWWYIkDJ/", thumbnail = icon05, fanart = fan01, folder = True)	
	plugintools.add_item(title = "[ Tendências - Paranóias ]", url = base + "playlist/PLAg4T2da6qWxSswYqS6gi4XYZ3qlz5Azo/", thumbnail = icon06, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Biografias - Eventos ]", url = base + "playlist/PLAg4T2da6qWzUkstE50-E3rRnLCW9nX2Q/", thumbnail = icon07, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Cultos - Seitas ]", url = base + "playlist/PLAg4T2da6qWw0Ur-IntdWEUylciQESGRK/", thumbnail = icon08, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Cosmos - Planetas ]", url = base + "playlist/PLAg4T2da6qWzckdBwDHweyF6hqds1NtAL/" , thumbnail = icon09, fanart = fan01, folder = True)	
	plugintools.add_item(title = "[ Era uma Vez ]", url = base + "playlist/PLAg4T2da6qWwLIP_kqJn5WIvZeqkg3aJ5/", thumbnail = icon10, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Revolução Ciêntifica ]", url = base + "channel/UCPLBXvobTRvDjPy41y9hG8g/", thumbnail = iconAB, fanart = fan01, folder = True)
	

	
	xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
