from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
def index(request):
	context = {
		'detail' : 'My name is Kaur',
		'detail2' : 'I like to code.'
	}
	return render(request, 'home/index.html', context)