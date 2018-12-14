import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT) #ERROR 2 - Not declaring the pin as output
GPIO.setup(24,GPIO.OUT)


def ActivateRed():
	GPIO.output(25,GPIO.HIGH)
	print "Red LED on"


def DeactivateRed():
	GPIO.output(25,GPIO.LOW)
	print "Red LED off"
	
def ActivateBlue():
	GPIO.output(24,GPIO.HIGH)
	print "Blue LED on"


def DeactivateBlue():
	GPIO.output(24,GPIO.LOW)
	print "Blue LED off"


if __name__ == "__main__":
	
	print "LED on"
	GPIO.output(25,GPIO.HIGH)
	time.sleep(1)
	print "LED off"
	GPIO.output(25,GPIO.LOW)
	print "LED on"
	GPIO.output(24,GPIO.HIGH)
	time.sleep(1)
	print "LED off"
	GPIO.output(24,GPIO.LOW)

