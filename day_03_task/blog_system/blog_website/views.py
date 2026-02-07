from django.shortcuts import render
from .models import BlogPost



# Create your views here.
def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'home.html' , {'posts': posts})

