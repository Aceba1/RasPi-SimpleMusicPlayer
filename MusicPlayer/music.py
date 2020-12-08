import os
import time

PATH = "/home/pi/music"

while True:
  time.sleep(1.00)
  files = os.listdir(PATH)
  print("Found " + str(len(files)) + " item(s) in " + PATH)
  for f in files:
    print("Playing " + f)
    os.system("mpg123 " + PATH + "/" + f)