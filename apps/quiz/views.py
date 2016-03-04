from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
# def index(request):
# 	return render(request, 'quiz/index.html')

# def show(request, question_id):
#   return HttpResponse("You are looking at question number %s." % question_id)


# Returning Errors
# Returning HTTP error codes in Django is easy. You can use  HttpResponse subclasses for a number of common HTTP status codes other than 200 (which means "OK"). For example (modify the show() method of your quiz app):
# def show(request, question_id):
#   if int(question_id) == 1:
#     return HttpResponse('<h1>Page found!</h1>')
#   else:
#     raise Http404

# Customized 404 Error Response
# For convenience, and because it's a good idea to have a consistent 404 error page across your site, Django provides an  Http404exception. If you raise Http404 at any point in a view function, Django will catch it and return the standard error page for your application, along with an HTTP error code 404. If you visit a link other than '/quiz/1', you would see a 404 page.
# def show(request, question_id):
#   if int(question_id) == 1:
#     return HttpResponse('<h1> Page found! </h1>')
#   else:
#     return HttpResponseNotFound('<h1> Page not found! </h1>')

def index(request):
  context = {
      'questions': [
           { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
           { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
           { 'id': 3, 'content': 'Why are they called apartments when they are all together?'},
           { 'id': 4, 'content': 'Why are cigarettes sold where smoking is prohibited?'},
       ]
  }
  return render(request, 'quiz/index.html', context)

def show(request, question_id):
  context = {
    'id': question_id,
    'question': "Why is a boxing ring square?",
  }
  return render(request, 'quiz/show.html', context)