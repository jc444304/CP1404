import csv

SONGS_CSV_FILE_NAME = "song.csv"

SONG_YEAR_MIN = 1000

"""

"""


def main():
	print("Songs to Learn - by Yvan Burrie")
	
	songs = []
	with open(SONGS_CSV_FILE_NAME, 'rb') as songsFile:
		spamreader = csv.reader(songsFile, delimiter=' ', quotechar='|')
		for row in spamreader:
			print(row)
	
	while True:
		showMainMenu()
		menuOption = input().lower()
		if menuOption == "l":
			showSongsList(songs)
		if menuOption == "a":
			showSongsAdd()
		if menuOption == "c":
		
		if menuOption == "q":
			break
	
	print("{} song(s) saved to ")

def showMainMenu():
	print("Please select the following options:")
	print("L - List songs")
	print("A - Add new song")
	print("C - Complete a song")
	print("Q - Quit")

def showSongsList(songs):
	songCount = songs.count()
	songsDone = getSongsDone()
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
	pass

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