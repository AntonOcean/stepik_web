from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from qa.models import *
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def notfount(request):
    return HttpResponseNotFound("Not Found!")

def questions_list(request):
    question = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(question, 10)
    paginator.baseurl = 'question/'
    page = paginator.page(page)
    return render(request, 'question_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def popular_list(request):
    question = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(question, 10)
    paginator.baseurl = 'question/'
    page = paginator.page(page)
    return render(request, 'question_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def question(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'question.html', {
        'question': question,
        'text': question.text,
        'title': question.title,
        'answers': question.answer_set.all(),
    })
# Create your views here.
