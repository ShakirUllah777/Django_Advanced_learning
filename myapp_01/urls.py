# used to add the endpoint urls for each app it will be diffirent 
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('index/' , views.index , name='index'),
]
