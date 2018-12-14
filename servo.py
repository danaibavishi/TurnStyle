import RPi.GPIO as GPIO
import time


servoPIN = 13
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(6.5) # Initialization


def closegate():
	p.ChangeDutyCycle(6)

def opengate():
	p.ChangeDutyCycle(11)

if __name__ == "__main__":
	try:
		while True:
			closegate()
			time.sleep(0.5)
			opengate()
			time.sleep(0.5)
	
	
	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()
