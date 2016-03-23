import urllib
from BeautifulSoup import *
import re

# url = "http://www.billboard.com/charts/hot-100"
url = "http://www.billboard.com/charts/rock-songs"

top = 20

class song():
	_songCount = 0

	def __init__(self):
		pass

	def setPos(self, position):
		for po in position:
			if po.get('class') == "chart-row__current-week":
				self.position = int(po.contents[0])
				# print 'pos',self.position

	def setSongName(self, songName):
		for name in songName:
			if name.get('class') == "chart-row__song":
				self.songName = str(name.contents[0])
				# print 'name',self.songName

	def setArtist(self, artist):
		for ist in artist:
			if ist.get('data-tracklabel') == "Artist Name":
				self.artist = str(ist.contents[0]).lstrip().rstrip()

	def setSpotifyId(self, links):
		for link in links:
			if link.get('title') == "Spotify":
				fullLink = link.get('href')
				Id = re.findall('track:(.+)', fullLink)
				self.spotifyId = Id[0]

def run(top):
	count = 0
	songs = []

	try: myWeb = urllib.urlopen(url).read()
	except: return 0
	# print myWeb
	soup = BeautifulSoup(myWeb)
	tags = soup('article')

	for tag in tags:
		# print tag.contents
		# print "\n\n\n\n\n"
		Asong = song()
		Asong.setPos(tag('span'))
		Asong.setSongName(tag('h2'))
		Asong.setArtist(tag('a'))
		Asong.setSpotifyId(tag('a'))
		songs.append(Asong)

	print '---------------------------------------'
	print 'Position\tSong -- Artist'
	print '---------------------------------------'
	for data in songs:
		try:
			pos = data.position
			name = data.songName
			artist = data.artist
			spotify = data.spotifyId
			print pos,'\t',name,'--',artist
			# print 'Spotify:', spotify,'\n'
		except: pass

		if pos == top:
			break
	return(songs)

if __name__ == "__main__":

	run(top)


