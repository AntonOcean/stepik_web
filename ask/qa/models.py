from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	title = models.CharField(default="", max_length=50)
	text = models.TextField(default="")
	added_at = models.DateField(null=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User, related_name="q_to_likes")
	objects = QuestionManager()

class Answer(models.Model):
	text = models.TextField(default="")
	added_at = models.DateField(null=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
# Create your models here.
