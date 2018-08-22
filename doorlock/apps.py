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
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(servo_pin, GPIO.OUT)
		GPIO.setup(led_pin, GPIO.OUT)
		self.led_pin=led_pin
		self.servo_pin=servo_pin
		self.servo = GPIO.PWM(servo_pin, 50)
		self.current_state=current_state
		print('main')
	
	def lockDoor(self):
		#self.servo.changeDutyCycle(lockState)
		GPIO.output(self.led_pin,GPIO.HIGH)
		print('lock')

		# set stall current zero
  
	def unlockDoor(self):
		#self.servo.changeDutyCycle(unlockState)
		GPIO.output(self.led_pin,GPIO.LOW)
		print('unlock')

	def changeState(self):
		
		if (self.current_state == '1'):
			print('0')
			self.unlockDoor()
			self.current_state = '0'
		else:
			print('1')
			self.lockDoor()
			self.current_state = '1'
			# notify
		return(self.current_state) 
		
		#print("Problem in Changing State")

	# def getCurrentState():
	# 	try:
