# Read json file
# from mfrc522 import SimpleMFRC522
# import RPi.GPIO as GPIO
import json


def readJson(file):
    with open(file) as json_file:
        data = json.load(json_file)
        print(data)
        return data


def writeJson(file, data):
    with open(file, "w") as outfile:
        json.dump(data, outfile)
        print("Write json file success")


def containSong(songs, song):
    for s in songs:
        if songs[s] == song:
            return True
    return False


songsName = readJson("songsNames.json")
songs = readJson("songs.json")
reader = SimpleMFRC522()
for key in songsName:
    if not containSong(songs, songsName[key]):
        # Read from the RFID reader
        print("Please scan the RFID card for song: " + key)
        id = reader.read()[0]
        # id = input()
        print("Card Value is:", id)
        songs[id] = songsName[key]
        writeJson("songs.json", songs)
        print("Write song " + key + " success")
    else:
        print("Song " + key + " existed")

# GPIO.cleanup()
