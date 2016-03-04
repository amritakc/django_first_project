from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from time import strftime
# Create your views here.
def index(request):
	context = {
        'current_date' : strftime("%B %d, %Y"),
        'current_time' :  strftime("%H:%M:%S")
	}
	return render(request, 'times/index.html', context)