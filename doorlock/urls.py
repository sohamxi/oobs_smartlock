from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^door/', views.changeState, name='changeState'),
]