import os
import time
import RPi.GPIO as GPIO

# Constants
GPIO_ECHO = 24
TIME_BETWEEN_VIDEOS = 10
VIDEO_PATH = "/home/pi/video"

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_ECHO, GPIO.IN)
os.system("clear")

# Sensor
def waitforsignal():
	while GPIO.input(GPIO_ECHO) == 1:
		pass #time.sleep(0.01)
	return

# Main loop
while True:
	items = os.listdir(VIDEO_PATH)
	for names in items:
		if names.endswith(".mp4"):
			waitforsignal()
			os.system("omxplayer " + VIDEO_PATH + "/" + names)
			os.system("clear")
			time.sleep(TIME_BETWEEN_VIDEOS)
	time.sleep(10)
