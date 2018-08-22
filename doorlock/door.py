#import RPi.GPIO as GPIO 
import time

class Door:
	""" This creates the main module of the door object
	"""

	lockState = 100
	unlockState = 1

	all_states = ['Locked','Unlocked']

	def __init__(self, servo_pin = 14,led_pin = 17,current_state):
		#self.current_state = self.getCurrentState()
		#self.servo = GPIO.PWM(servo_pin, 50)
		#GPIO.setup(led_pin, GPIO.OUT)
		self.current_state=current_state
		print ('main')
	def lockDoor(self):
		print('lock fun')
		#self.servo.changeDutyCycle(lockState)
		#GPIO.output(led_pin,1)
		

		# set stall current zero
  
	def unlockDoor(self):
		print('unlock fun')
		#self.servo.changeDutyCycle(unlockState)
		#GPIO.output(led_pin,0)

	def changeState(self):
		try:
			if (self.current_state == '1'):
				print('Test1')
				self.unlockDoor()
				self.current_state = '0'
			else:
				print('Test2')
				self.lockDoor()
				self.current_state = '1'
			# notify
			return(self.current_state) 
		except:
			print("Problem in Changing State")

	# def getCurrentState():
	# 	try:

