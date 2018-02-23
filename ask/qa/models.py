from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = models.CharField(max_length=50)
	likes = models.ForeignKey(User)
	objects = QuestionManager()

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question)
	author = models.CharField(max_length=50)
# Create your models here.
