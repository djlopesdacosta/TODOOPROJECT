import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import urllib2,urllib

AddonTitle="[COLOR ghostwhite]Project X[/COLOR] [COLOR lightsteelblue]Wizard[/COLOR]"

if xbmc.getCondVisibility('system.platform.ios') or xbmc.getCondVisibility('system.platform.osx'):
	Repo = "http://teamtuga4ever.net23.net/teamtuga4ever.repository/addons.xml"
	Beta = "http://teamtuga4ever.net23.net/ProjectXwizard/Beta.xml"
	Website = "http://www.team-tuga4ever.16mb.com/"
	Forum = "http://tvsupertuga.forum-gratuito.com/"
	Community = "https://www.facebook.com/groups/1735809796639007/"
	JarvisWiz = "http://teamtuga4ever.net23.net/ProjectXwizard/JarvisWiz.xml"
	JarvisCheck = "http://teamtuga4ever.net23.net/ProjectXwizard/JarvisCheck.xml"
	JarvisUpdate = "http://teamtuga4ever.net23.net/ProjectXwizard/JarvisUpdate.xml"
	KryptonWiz = "http://teamtuga4ever.net23.net/ProjectXwizard/KryptonWiz.xml"
	KryptonCheck = "http://teamtuga4ever.net23.net/ProjectXwizard/KryptonCheck.xml"
	KryptonUpdate = "http://teamtuga4ever.net23.net/ProjectXwizard/KryptonUpdate.xml"
else:
	Repo = "http://teamtuga4ever.net23.net/teamtuga4ever.repository/addons.xml"
	Beta = "http://teamtuga4ever.net23.net/ProjectXwizard/Beta.xml"
	Website = "http://www.team-tuga4ever.16mb.com/"
	Forum = "http://tvsupertuga.forum-gratuito.com/"
	Community = "https://www.facebook.com/groups/1735809796639007/"
	JarvisWiz = "http://teamtuga4ever.net23.net/ProjectXwizard/JarvisWiz.xml"
	JarvisCheck = "http://teamtuga4ever.net23.net/ProjectXwizard/JarvisCheck.xml"
	JarvisUpdate = "http://teamtuga4ever.net23.net/ProjectXwizard/JarvisUpdate.xml"
	KryptonWiz = "http://teamtuga4ever.net23.net/ProjectXwizard/KryptonWiz.xml"
	KryptonCheck = "http://teamtuga4ever.net23.net/ProjectXwizard/KryptonCheck.xml"
	KryptonUpdate = "http://teamtuga4ever.net23.net/ProjectXwizard/KryptonUpdate.xml"

def Check():

	RepoStatus = "[COLOR lime]ONLINE[/COLOR]"
	BetaStatus = "[COLOR lime]ONLINE[/COLOR]"
	JarvisWizStatus = "[COLOR lime]ONLINE[/COLOR]"
	JarvisCheckStatus = "[COLOR lime]ONLINE[/COLOR]"
	JarvisUpdateStatus = "[COLOR lime]ONLINE[/COLOR]"
	KryptonWizStatus = "[COLOR lime]ONLINE[/COLOR]"
	KryptonCheckStatus = "[COLOR lime]ONLINE[/COLOR]"
	KryptonUpdateStatus = "[COLOR lime]ONLINE[/COLOR]"
	WebsiteStatus = "[COLOR lime]ONLINE[/COLOR]"
	ForumStatus = "[COLOR lime]ONLINE[/COLOR]"
	CommunityStatus = "[COLOR lime]ONLINE[/COLOR]"

	dialog = xbmcgui.Dialog()

	xbmc.executebuiltin( "ActivateWindow(busydialog)" )

	try:
		response = urllib2.urlopen(Repo)
	except:
		RepoStatus = "[COLOR red]OFFLINE[/COLOR]"
	
	try:
		response = urllib2.urlopen(Beta)
	except:
		BetaStatus = "[COLOR red]OFFLINE[/COLOR]"
	
	try:
		response = urllib2.urlopen(JarvisWiz)
	except:
		JarvisWizStatus = "[COLOR red]OFFLINE[/COLOR]"
	
	try:
		response = urllib2.urlopen(JarvisCheck)
	except:
		JarvisCheckStatus = "[COLOR red]OFFLINE[/COLOR]"
	
	try:
		response = urllib2.urlopen(JarvisUpdate)
	except:
		JarvisUpdateStatus = "[COLOR red]OFFLINE[/COLOR]"
	
	try:
		response = urllib2.urlopen(KryptonWiz)
	except:
		KryptonWizStatus = "[COLOR red]OFFLINE[/COLOR]"
	
	try:
		response = urllib2.urlopen(KryptonCheck)
	except:
		KryptonCheckStatus = "[COLOR red]OFFLINE[/COLOR]"
	
	try:
		response = urllib2.urlopen(KryptonUpdate)
	except:
		KryptonUpdateStatus = "[COLOR red]OFFLINE[/COLOR]"
		
	try:
		response = urllib2.urlopen(Website)
	except:
		WebsiteStatus = "[COLOR red]OFFLINE[/COLOR]"
		
	try:
		response = urllib2.urlopen(Forum)
	except:
		ForumStatus = "[COLOR red]OFFLINE[/COLOR]"
		
	try:
		response = urllib2.urlopen(Community)
	except:
		CommunityStatus = "[COLOR red]OFFLINE[/COLOR]"

	xbmc.executebuiltin( "Dialog.Close(busydialog)" ) 

	dialog.ok(AddonTitle + " - Page 1 of 4","[COLOR lightsteelblue]Website: " + WebsiteStatus ,"Forum: " + ForumStatus,"Community Builds: " + CommunityStatus)
	dialog.ok(AddonTitle + " - Page 2 of 4","[COLOR lightsteelblue]Repository: " + RepoStatus ,"BETA Builds: " + BetaStatus)
	dialog.ok(AddonTitle + " - Page 3 of 4","[COLOR lightsteelblue]Jarvis Builds: " + JarvisWizStatus ,"Jarvis Version Checker: " + JarvisCheckStatus,"Jarvis Updater: " + JarvisUpdateStatus)
	dialog.ok(AddonTitle + " - Page 4 of 4","[COLOR lightsteelblue]Krypton Builds: " + KryptonWizStatus ,"Krypton Version Checker: " + KryptonCheckStatus,"Krypton Updater: " + KryptonUpdateStatus)
