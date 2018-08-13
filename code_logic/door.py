import RPi.GPIO as GPIO 

class Door:
	""" This creates the main module of the door object
	"""

	lockState = 800
	unlockState = 2500

	all_states = ['Locked','Unlocked']

	def __init__(self, servo_pin = 14,led_pin = 17,current_state):
		self.current_state = self.getCurrentState()
		self.servo = GPIO.setup(servo_pin, GPIO.OUT)
		self.led = GPIO.setup(led_pin, GPIO.OUT)

	def lockDoor(self):
		motor.servoWrite(lockState)
		led.digitalWrite(1)
		self.changeState()

		# notify

		# set stall current zero

	def unlockDoor(self):
		motor.servoWrite(unlockState)
		led.digitalWrite(0)
		self.changeState()	


