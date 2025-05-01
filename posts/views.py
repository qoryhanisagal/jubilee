from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(CreateView):
    """
    View to create a new post.
    """
    model = Post
    fields = ['title', 'subtitle', 'body', 'author', 'status']
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts:post_list')

class PostUpdateView(UpdateView):
    """
    View to update a post.
    """
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']
    template_name = 'posts/post_edit.html'

class PostDeleteView(DeleteView):
    """
    View to delete a post.
    """
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:post_list')
