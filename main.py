import csv

SONGS_CSV_FILE_NAME = "song.csv"

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
	for song in songs:
		print("{} {} {} {}".format(song['Title'], song['Artist'], song['Year'], song['Done']))

def showSongsAdd():
	pass

def showSongsDone():
	pass

main()