from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'question.html', {
        'form': form,
        'question': question,
        'text': question.text,
        'title': question.title,
        'answers': question.answer_set.all(),
        'author': request.user
    })

def question_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            ask = form.save()
            url = ask.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form,
        'author': request.user,
        'session': request.session
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form,
    })

def loginup(request):
    error = ''
    if request.method == 'POST':
        login_user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=login_user, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect('/')
            return response
        else:
            error = 'Error'
            form = LoginForm()
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'error': error,
        'form': form,
    })
# Create your views here.
