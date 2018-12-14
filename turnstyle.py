import RPi.GPIO as GPIO
import time
import servo
import distance_sensor as ds
import ledcontrol as led
from espeak import espeak

"""
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN_TRIGGER = 4
PIN_ECHO = 17
servoPIN = 13

GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.setup(servoPIN, GPIO.OUT)

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
print "Waiting for sensor to settle"
time.sleep(2)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
"""
said = 1

if __name__ == '__main__':
		while True:
			servo.closegate()
			distance = ds.getdistance() #ERROR 1 - no writing the ds 
			print distance # Remove for error 3
			if distance < 20:
				if said == 0:
					espeak.synth("Welcome you beautiful people")
					said = 1
				servo.opengate()
				led.DeactivateRed()
				led.ActivateBlue()
				time.sleep(1)
			else:
				if said == 1:
					espeak.synth("Gate closed, See you next time")
					said = 0 
				servo.closegate()
				led.DeactivateBlue()
				led.ActivateRed()
				time.sleep(1)
