from django.shortcuts import redirect, render
from quiz.models import Topic, Choice

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Topic.objects.create(post_text=request.POST['name_quiz'])
        return redirect('/')
    question = Topic.objects.all()
    return render(request, 'home.html', {'question': question})
    #return render(request, 'home.html')

def detail(request, question__id):
    #items = Topic.objects.get(id=item_id)
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question__id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
