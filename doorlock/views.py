from doorlock.apps import Door
import RPi.GPIO as GPIO 
from django.http import HttpResponse

def changeState(request):
	req = request.GET['val']
	print(type(req))
	if req == '1':
		current_state = '1'
	else:
		current_state='0'
	door=Door(current_state)
	new_state=door.changeState()
	return HttpResponse('The door is now {}'.format(new_state))
