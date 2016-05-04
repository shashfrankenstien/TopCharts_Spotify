import BillboardWebScraper
import os
import webbrowser

top = 25

spotifyUrl = "http://open.spotify.com/track/"


def err():
	print 'Error in entry! Restarting application'
	execute()

def openSpotify(Id):
	url = spotifyUrl+Id
	print "opening in Spotify web app..."
	webbrowser.open(url)

def playASong(songs):
	play = raw_input("\nType in a Position number to listen to the song on Spotify: ")
	try:
		play = int(play)
	except: err()

	for song in songs:
		try:
			if (song.position == play):
				openSpotify(song.spotifyId)
		except: pass
	execute()

def execute():
	os.system('clear')
	print "######## -- Billboard Top",top, "Songs -- ########"
	print '--------------------------------------------'
	print "(Requires a working internet connection)"
	print "Fetching this week's top", top,"songs from Billboard.com...\n"
	songs = BillboardWebScraper.run(top)
	if songs == 0:
		print "No internet connection found.\n Terminating application"
		quit()
	else: playASong(songs)

	

if __name__ == "__main__":
	execute()