from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,redirect, render
from quiz.models import Topic, Choice
from django.urls import reverse

# Create your views here.
def home_page(request):
    question = Topic.objects.all()
    return render(request, 'home.html', {'question': question})
    #return render(request, 'home.html')

#create question
def create_quiz(request):
    if request.method == 'POST':
        T = Topic(post_text=request.POST['name_quiz'],
            ans=request.POST['choice'])
        T.save()
        Ans_T = Choice(choice_text='true',
        topic=T, votes='0')
        Ans_F = Choice(choice_text='fales',
        topic=T, votes='0')
        Ans_T.save()
        Ans_F.save()
        return redirect('/')
    
    return render(request, 'create.html')


#Show detail of Topic
def detail(request, question_id):
    question = Topic.objects.get(id=question_id)
    
    return render(request, 'detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

#แสดงผลโหวตและมีปุ่มกลับไปโหวตใหม่และไปที่หน้า home
def results(request, question_id):
    question = get_object_or_404(Topic, pk=question_id)
    return render(request, 'result.html', {'question' : question})

#ฟังก์ชันสำหรับโหวต เมื่อกดโหวตแล้วจะ redirect ไปที่หน้าแสดงผลโหวต
def vote(request, question_id):
    question = get_object_or_404(Topic, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question' : question,
            'error_massage' : "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
