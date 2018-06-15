from django.db import models

# Create your models here.
class Topic(models.Model):
    post_text = models.TextField(default='')
    ans = models.TextField(default='')

#เก็บคนที่โหวตแต่ละคำตอบ
class Choice(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

#เก็บผลตอบถูก ตอบผิด
class Answer(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	ans_text = models.CharField(max_length=200)
	ans_vote = models.IntegerField(default=0)