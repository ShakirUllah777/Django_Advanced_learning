# used to write the urls endpoint fuction and its logic here ----------
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World!')

def index(request):
    return HttpResponse('This is the Index url Page!')