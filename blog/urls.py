from django.urls import path
from . import views


urlpatterns = [
    path('' , views.blog_home , name='blog_home'),
    path('blog_index', views.blog_index , name='blog_index'),
]
