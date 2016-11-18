# -*- coding: utf-8 -*-

'''
    zen Add-on
    Copyright (C) 2016 zen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import re,urllib,urlparse,random
from resources.lib.modules import cleantitle
from resources.lib.modules import client


class source:
    def __init__(self):
        self.domains = ['1fardadownload.net']
        self.movie_link = 'http://dl.uplodin.ir/Film/%s/'
        self.series_link = 'http://dl.uplodin.ir'
        self.search_link = '/?blogs=1%2C5&s='


    def movie(self, imdb, title, year):
        self.zen_url = []	
        try:
			self.zen_url = []
			title = cleantitle.getsearch(title)
			# print ("FDL MOVIES", title)
			cleanmovie = cleantitle.get(title)
			
			query = self.movie_link % year
			
			print ("FDL MOVIES", query)
			mylink = client.request(query)
			match = re.compile('href="([^"]+)"').findall(mylink)
			for movielink in match:
				if year in movielink:
					item_title = cleantitle.get(movielink)
					if cleanmovie in item_title:
						href = urlparse.urljoin(query, movielink)
						print ("FDL MOVIES", href)
						self.zen_url.append(href)
			return self.zen_url
        except:
            return
			
			
    def tvshow(self, imdb, tvdb, tvshowtitle, year):
        try:
            url = {'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return			

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        self.zen_url = []		
        try:
            self.zen_url = []
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']

            cleanmovie = cleantitle.get(title)


            season = '%02d' % int(season)
            episode = '%02d' % int(episode)
            checkepisode = "s" + season + "e" + episode
            query = "/Serial/"
            # print("FDL EPISODES", query)
            query = self.series_link + query
            link = client.request(query)
            r = client.parseDOM(link, 'a', ret = 'href')
            for items in r:
				try:
					items = items.encode('utf-8')
					items_clean = urllib.unquote(items)
					# print("FDL EPISODES", items)
					if cleanmovie in cleantitle.get(items_clean):
						# print("FDL EPISODES", items)
						seasonquery = "S%s/" % season
						items = items.replace(' ','%20')
						finalquery = query + items + seasonquery
						# print("FDL EPISODES", finalquery)

						link2 = client.request(finalquery)
						r2 = client.parseDOM(link2, 'a', ret = 'href')
						for links in r2:
							vid_url = links.encode('utf-8')
							if checkepisode in cleantitle.get(vid_url):
								movielink = finalquery + vid_url
								title = vid_url + "=episode"
								self.zen_url.append([movielink,title])
				except:
					pass
            print("FDL passed EPISODES", self.zen_url)
            return self.zen_url
        except:
            return		
			

    def sources(self, url, hostDict, hostprDict):
        try:
			sources = []

			for url in self.zen_url:
				print ("FDL URLS", url)
				if "1080" in url: quality = "1080p"
				elif "720" in url: quality = "HD"				
				else: quality = "SD"					
				if not any(value in url for value in ['imagebam','imgserve','histat','crazy4tv','facebook','.rar', 'subscene','.jpg','.RAR', 'postimage', 'safelinking','linx.2ddl.ag','upload.so','.zip', 'go4up','imdb']):
					if any(value in url for value in hostprDict):
							
						print ("FDL URLS", url)
						sources.append({'source': 'cdn', 'quality': quality, 'provider': 'Fdl', 'url': url, 'direct': True, 'debridonly': False})

			return sources
        except:
            return sources


    def resolve(self, url):
        return url
        
