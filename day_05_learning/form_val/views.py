from django.shortcuts import render , redirect, get_object_or_404
from .forms import Postform
from .models import Post
from django.contrib import messages


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})


def post_create(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'post created succesfully')
            return redirect('post_list')
        else:
            messages.error(request, 'Please correct the error')

    else:
        form = Postform()

    return render(request, 'post_form.html', {'form':form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('post_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = Postform(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})