from django.shortcuts import render
from quiz.models import Topic

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def detail(request, question__id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question__id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
