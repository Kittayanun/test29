from django.db import models

# Create your models here.
class Topic(models.Model):
    post_text = models.TextField(default='')

class Choice(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
