from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,redirect, render
from quiz.models import Topic, Choice, Answer
from django.urls import reverse

# Create your views here.
def home_page(request):
    question = Topic.objects.all()
    return render(request, 'home.html', {'question': question})
    #return render(request, 'home.html')

#create question
def create_quiz(request):
    if request.method == 'POST':
        #create Question
        Q = Topic(post_text=request.POST['name_quiz'],
            ans=request.POST['choice'])
        Q.save()

        #create choice
        choice_1 = Choice(choice_text='True',
            topic=Q, votes='0')
        choice_2 = Choice(choice_text='False',
            topic=Q, votes='0')
        choice_1.save()
        choice_2.save()

        #create Correct,Uncorrect answer
        Correct_ans = Answer(ans_text='Correct',
            topic=Q, ans_vote='0')
        Uncorrect_ans = Answer(ans_text='Uncorrect',
            topic=Q, ans_vote='0')
        Correct_ans.save()
        Uncorrect_ans.save()

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
        #selected choice
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #Correct Answer
        correct_ans_forQuiz = question.ans
        #ตอบถูก ตอบผิด
        ans_correct = question.answer_set.get(ans_text='Correct')
        ans_uncorrect = question.answer_set.get(ans_text='Uncorrect')
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if correct_ans_forQuiz == selected_choice.choice_text:
            ans_correct.ans_vote += 1
            ans_correct.save()
        elif correct_ans_forQuiz != selected_choice.choice_text:
            ans_uncorrect.ans_vote += 1
            ans_uncorrect.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
