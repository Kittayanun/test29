from django.db import models

# Create your models here.
class Topic(models.Model):
    post_text = models.TextField(default='')
