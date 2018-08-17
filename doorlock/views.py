from doorlock.apps import Door
import RPi.GPIO as GPIO 
from django.http import HttpResponse

def changeState(request):
	req = request.GET.get('val','')
	if req == '1':
		current_state = 'Locked'
	else:
		current_state='Unlocked'
	door=Door(current_state)
	new_state=door.changeState()
	return HttpResponse('The door is now {}'.format(new_state))