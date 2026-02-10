from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 5   # 5 posts per page
    ordering = ['-created_at']  # latest first

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Post.objects.all().order_by('-created_at')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )
        return queryset

    
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_form.html"

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_form.html"


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = "post_confirm_delete.html"



