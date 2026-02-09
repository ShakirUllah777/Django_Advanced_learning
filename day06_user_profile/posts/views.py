from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def create_post(request):
    if request.method == "POST":
        Post.objects.create(
            user=request.user,
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('my_posts')
    return render(request, 'posts/create_post.html')

@login_required
def my_posts(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/my_posts.html', {'posts': posts})

@login_required
def edit_post(request, id):
    post = Post.objects.get(id=id, user=request.user)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('my_posts')
    return render(request, 'posts/edit_post.html', {'post': post})
