# used to write the urls endpoint fuction and its logic here ----------
from django.shortcuts import render


def home(request):
    items = ['Laptop', 'Mobile', 'Tablet', 'Headphones']
    return render(request , 'home.html' , {'items':items})

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')




