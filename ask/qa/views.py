from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def notfount(request):
    return HttpResponseNotFound("Not Found!")
# Create your views here.
