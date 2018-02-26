from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from qa.models import *
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def notfount(request):
    return HttpResponseNotFound("Not Found!")

def quetions_list(request):
    question = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(question, 10)
    paginator.baseurl = 'question/'
    page = paginator.page(page)
    return render(request, 'question_list.html', {
        'questins': page.object_list,
        'paginatior': paginator,
        'page': page,
    })
# Create your views here.
