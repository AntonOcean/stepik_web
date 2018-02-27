from django import forms
from qa.models import *

class AskForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        return self.cleaned_data
    def save(self):
        question = Question.objects.create(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question
    def clean(self):
        return self.cleaned_data
    def save(self):
        answer = Answer.objects.create(**self.cleaned_data)
        answer.save()
        return answer