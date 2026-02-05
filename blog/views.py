from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def blog_home(request):
    return HttpResponse('WellCome to Blog App Home Page!')

def blog_index(request):
    return HttpResponse('This is Blog index Page!')