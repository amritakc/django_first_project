from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
	return render(request, 'ninja/index.html')

# def show(request, color):
# 	# context = {
# 	# 	'id' : color_id
# 	# }
# 	return render(request, 'ninja/show.html')
# def show(request, color_id):
#   context = {
#     'id': color_id,
#     'question': "Why is a boxing ring square?",
#   }
#   return render(request, 'quiz/show.html', context)

def show(request, color):
	if color == 'blue':
		return HttpResponse("<img src = '/static/ninja/blue.jpg'>")
	elif color == 'red':
		return HttpResponse("<img src = '/static/ninja/red.jpg'>")
	elif color == 'orange':
		return HttpResponse("<img src = '/static/ninja/orange.jpg'>")
	elif color == 'purple':
		return HttpResponse("<img src = '/static/ninja/purple.jpg'>")
	else:
		return HttpResponse("<img src = '/static/ninja/megan_fox.jpg'>")