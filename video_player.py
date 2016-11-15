# External module imports
import time
import RPi.GPIO as GPIO
import sys
import os
import subprocess
from subprocess import Popen

GPIO.setwarnings(False)
# Pin Definitons
#LEDs
buttonLed1 = 22
buttonLed2 = 23
buttonLed3 = 20
buttonLed4 = 21 

#buttons
button1 = 12 
button2 = 13 
button3 = 16 
button4 = 17 

# Pin Setup
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(buttonLed1, GPIO.OUT) # LED pin set as output
GPIO.setup(buttonLed2, GPIO.OUT) # LED pin set as output
GPIO.setup(buttonLed3, GPIO.OUT) # LED pin set as output
GPIO.setup(buttonLed4, GPIO.OUT) # LED pin set as output

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w pull-up
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w pull-up
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w pull-up
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w pull-up

# Initial state for LEDs
GPIO.output(buttonLed1, GPIO.LOW)
GPIO.output(buttonLed2, GPIO.LOW)
GPIO.output(buttonLed3, GPIO.LOW)
GPIO.output(buttonLed4, GPIO.LOW)

# Video assignment
movie1 = '/home/pi/code/video/4.mp4'
movie2 = '/home/pi/code/video/5.mp4'
movie3 = '/home/pi/code/video/6.mp4'
movie4 = '/home/pi/code/video/7.mp4'
movie5 = '/home/pi/code/video/8.mp4'

#tracking functions
play = False
stop = True

while True:
	if GPIO.input(button1):
		time.sleep(.01)
		print "Not Pressed"		
	else:
		GPIO.output(buttonLed1, GPIO.HIGH)
		GPIO.output(buttonLed2, GPIO.LOW)
		GPIO.output(buttonLed3, GPIO.LOW)
		GPIO.output(buttonLed4, GPIO.LOW)
		os.system('killall omxplayer.bin')
		time.sleep(2)
		omxp = Popen(['omxplayer',movie1])
		time.sleep(1)
		
	if GPIO.input(button2):		
		time.sleep(.01)
		print "Not Pressed"		
	else:
		GPIO.output(buttonLed1, GPIO.LOW)
		GPIO.output(buttonLed2, GPIO.HIGH)
		GPIO.output(buttonLed3, GPIO.LOW)
		GPIO.output(buttonLed4, GPIO.LOW)
		os.system('killall omxplayer.bin')
		time.sleep(2)
		omxp = Popen(['omxplayer',movie2])
		time.sleep(1)
	if GPIO.input(button3):		
		time.sleep(.01)
		print "Not Pressed"		
	else:
		GPIO.output(buttonLed1, GPIO.LOW)
		GPIO.output(buttonLed2, GPIO.LOW)
		GPIO.output(buttonLed3, GPIO.HIGH)
		GPIO.output(buttonLed4, GPIO.LOW)
		os.system('killall omxplayer.bin')
		time.sleep(2)
		omxp = Popen(['omxplayer',movie3])
		time.sleep(1)		
	if GPIO.input(button4):
		time.sleep(.01)
		print "Not Pressed"
		
	else:		
		GPIO.output(buttonLed1, GPIO.LOW)
		GPIO.output(buttonLed2, GPIO.LOW)
		GPIO.output(buttonLed3, GPIO.LOW)
		GPIO.output(buttonLed4, GPIO.HIGH)
		os.system('killall omxplayer.bin')
		time.sleep(2)
		omxp = Popen(['omxplayer',movie4])
		time.sleep(1)
		
		
		
		
		
		
	#if GPIO:
		#print "THIS IS PLAYING THE SPLASH"
		#os.system('killall omxplayer.bin')
		#time.sleep(2)
		#omxp = Popen(['omxplayer',movie5])
		#time.sleep(1)
		
		
		
		
		
		
		
		
		
time.sleep(.01)	

	
	


