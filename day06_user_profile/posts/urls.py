from django.urls import path
from .views import create_post, my_posts, edit_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('mine/', my_posts, name='my_posts'),
    path('edit/<int:id>/', edit_post, name='edit_post'),
]
