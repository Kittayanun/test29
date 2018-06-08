from django.shortcuts import redirect, render
from quiz.models import Topic, Choice

# Create your views here.
def home_page(request):
    question = Topic.objects.all()
    return render(request, 'home.html', {'question': question})
    #return render(request, 'home.html')

#create question
def create_quiz(request):
    if request.method == 'POST':
        Topic.objects.create(post_text=request.POST['name_quiz'],
            ans=request.POST['choice'])
        return redirect('/')
    return render(request, 'create.html')

def detail(request, question__id):
    question = Topic.objects.get(id=question__id)
    return render(request, 'detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question__id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
