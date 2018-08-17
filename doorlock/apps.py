from django.apps import AppConfig
import RPi.GPIO as GPIO 
import time


class doorlockConfig(AppConfig):
    name = 'doorlock'

class Door:
	""" This creates the main module of the door object
	"""

	lockState = 100
	unlockState = 1

	all_states = ['Locked','Unlocked']

	def __init__(self, current_state, servo_pin = 14,led_pin = 17):
		#self.current_state = self.getCurrentState()
		self.servo = GPIO.PWM(servo_pin, 50)
		GPIO.setup(led_pin, GPIO.OUT)
		self.current_state=current_state
	
	def lockDoor(self):
		self.servo.changeDutyCycle(lockState)
		GPIO.output(led_pin,1)
		

		# set stall current zero
  
	def unlockDoor(self):
		self.servo.changeDutyCycle(unlockState)
		GPIO.output(led_pin,0)

	def changeState(self):
		try:
			if (self.current_state == 'Locked'):
				self.unlockDoor()
				self.current_state == 'Unlocked'
			else:
				self.lockDoor()
				self.current_state == 'Locked'
			# notify
			return(self.current_state) 
		except:
			print("Problem in Changing State")

	# def getCurrentState():
	# 	try: