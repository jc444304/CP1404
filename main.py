import csv



SONGS_FILE = "songs.csv"

SONG_YEAR_MIN = 1000

SONGS_INVALID_CHARS = [
	""
]

"""

"""
def main():
	print("Songs to Learn - by Yvan Burrie")
	
	songs = []
	try:
		with open(SONGS_FILE, 'r') as songsFile:
			songsReader = csv.reader(songsFile, delimiter="\t")
			for songRaw in songsReader:
				songs.append({
					"Title": songRaw[0],
					"Artist": songRaw[1],
					"Year": songRaw[2],
					"Done": songRaw[3],
				})
	except IOError:
		print("Failed to open file '{}' for reading.".format(SONGS_FILE))
	
	while True:
		showMainMenu()
		menuOption = input().lower()
		if menuOption == "l":
			show_songs_list(songs)
		if menuOption == "a":
			showSongsAdd()
		if menuOption == "c":
			showSongsDone(songs)
		if menuOption == "q":
			break
	songsCount = songs.count(songs)
	songId = 0
	try:
		with open(SONGS_FILE, 'w') as songsFile:
			songId += 1
			song = songs[songId]
			songsWriter = csv.writer(songsFile)
			songRaw = [
				song['Title']
			]
			songsWriter.writerow(songRaw)
	except IOError:
		print("Failed to open file '{}' for reading.".format(SONGS_FILE))
	print("{} song(s) saved to ")

def showMainMenu():
	print("Please select the following options:")
	print("L - List songs")
	print("A - Add new song")
	print("C - Complete a song")
	print("Q - Quit")


def show_songs_list(songs):
	songCount = songs.count(songs)
	songsDone = getSongsDone(songs)
	for song in songs:
		print("{} {} {} {}".format(song['Title'], song['Artist'], song['Year'], song['Done']))
	print("{} song(s) learned, {} song(s) still to learn.".format(songsDone, songCount - songsDone))
	
def getSongsDone(songs):
	songsDone = 0
	for song in songs:
		if song['Done']:
			songsDone += 1
	return songsDone

def showSongsAdd():
	print("Attempting to add song...")
	while True:
		songTitle = input("Title: ")
		if not songTitle:
			print("Title must not be empty!")
			continue
		songArtist = input("Artist: ")
		if not songArtist:
			print("Artist must be empty!")
			continue
		print("")
	songs.append({
		"Title": songTitle,
	})

def showSongsDone(songs):
	songsCount = songs.count()
	while True:
		songId = input("Enter the number of a song to mark as learned")
		if songId.isdigit():
			songId = int(songId)
		else:
			print("Song ID must be an number!")
			continue
		if songId < 0 or songId >= songsCount:
			print("Song ID provided does not exist!")
			continue
		song = songs[songId]
		song['Done'] = True
		print("Song '{} (by {})' now learned.".format(song['Title'], song['Artist']))
		break

main()
