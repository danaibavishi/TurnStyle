#!/usr/bin/python
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

PIN_TRIGGER = 4
PIN_ECHO = 17

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
print "Waiting for sensor to settle"
time.sleep(2)



def getdistance():
	print "Calculating distance"
	GPIO.output(PIN_TRIGGER, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(PIN_TRIGGER, GPIO.LOW)
      	while GPIO.input(PIN_ECHO)==0:
		pulse_start_time = time.time()
      	while GPIO.input(PIN_ECHO)==1:
		pulse_end_time = time.time()
	pulse_duration = pulse_end_time - pulse_start_time
	dist = round(pulse_duration * 17150, 2)#Not obvious, return a string instead of dist. 
	return dist #ERROR 3 - The invisible failure. 

if __name__ == '__main__':
	try:
		while True:
			distance = getdistance()
			print "Distance:",distance,"cm"
			time.sleep(1)

	finally:
      		GPIO.cleanup()
