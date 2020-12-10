import os
import time
from datetime import datetime
from numpy import random
from mpyg321.mpyg321 import MPyg321Player

# Globals

PATH = "/home/pi/music"
#FADEOUT = 15_000
WAIT_ON_ACTIVE = 2_000
WAIT_ON_IDLE = 15_000
WAIT_ON_DEACTIVATE = 60_000
WAIT_ON_SHUFFLE = 1_000

lastSong = ""
canPlay = False
files = os.listdir(PATH)
player = MPyg321Player()

# Initialize

if len(files) == 0:
  print("No songs found in " + PATH + "! Exiting...")
  exit()

print("Found " + str(len(files)) + " item(s) in " + PATH)

# Methods

def stopPlaying():
  global player
  player.stop()

def checkCanPlay():
  global canPlay

  now = datetime.now()
  #now = time.localtime()
  weekDay = now.weekday()
  current = now.hour * 100 + now.minute

  print(weekDay)
  print(current)

  if weekDay == 6: # Sunday
    canPlay = False # No music on Sunday

  elif weekDay >= 0 and weekDay <= 4: # Monday - Friday
    canPlay = (current > 8_00 and current < 11_30) \
        or (current > 12_40 and current < 17_00)

  elif (weekDay == 5): # Saturday
    canPlay = (current > 8_20 and current < 4_00)

  return canPlay

def playSongs():
  global lastSong
  global canPlay

  random.shuffle(files)
  while files[0] == lastSong:
    random.shuffle(files)

  for f in files:
    if not canPlay:
      return

    print("Playing " + f)
    player.play_song(PATH + "/" + f)

    while player.status == 1: # 1:Playing
      time.sleep(WAIT_ON_ACTIVE)
      if not checkCanPlay():
        stopPlaying()
        break

    lastSong = f

def main():
  global canPlay

  while True:
    # Main loop
    while checkCanPlay():
      print("Shuffling queue")
      playSongs()
      time.sleep(WAIT_ON_SHUFFLE)

    print("Exited time")
    time.sleep(WAIT_ON_DEACTIVATE)
    while not checkCanPlay():
      time.sleep(WAIT_ON_IDLE)

# Run
main()