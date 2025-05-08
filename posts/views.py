from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Status
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

# List views
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the actual Status object for 'Published' (capitalized as stored in DB)
        published_status = Status.objects.get(name="Published")
        
        # Add data to the template context
        context['title'] = "Published Posts"
        context['post_list'] = Post.objects.filter(status=published_status).order_by('-created_on')
        
        return context
    
# Detail view
class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/post_list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name="Draft")
        context["title"] = "My Drafts"
        context["post_list"] = Post.objects.filter(
            status=draft,
            author=self.request.user
        ).order_by("-created_on")
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/post_list.html"  # Reuse your list template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived_status = Status.objects.get(name="Archived")
        context["title"] = "Archived"
        context["post_list"] = Post.objects.filter(
            status=archived_status
        ).order_by("-created_on")
        return context
    
# Create / Update / Delete views
class PostDetailView(UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def test_func(self):
        post = self.get_object()
        status_name = post.status.name

        if status_name == "Published":
            return True
        elif status_name == "Draft" and post.author == self.request.user:
            return True
        elif status_name == "Archived" and self.request.user.is_authenticated:
            return True
        else:
            return False


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new post.
    """
    model = Post
    fields = ['title', 'subtitle', 'body', 'author', 'status']
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts:post_list')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to update a post.
    """
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']
    template_name = 'posts/post_edit.html'
    
    def test_func(self):
        post = self.get_object()
        # Allow update if the user is the author of the post
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete a post.
    """
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:post_list')
    
    def test_func(self):
        post = self.get_object()
        # Allow delete if the user is the author of the post
        return post.author == self.request.user
    
# Test view for 403 Forbidden
    
def test_403_view(request):
    raise PermissionDenied


# Scratchpad for Testing and Understanding
# Illustrating with real-life case to help to understand better.
# Let's say we have a blog where users can create posts.
# Each post has an author, and we want to ensure that only the author can edit or delete their own posts.
# We can use Django's built-in UserPassesTestMixin to create a custom permission check.
# This mixin allows us to define a test_func method that checks if the user has permission to perform the action.
# In this case, we want to check if the user is the author of the post they are trying to edit or delete.
# We can use the UserPassesTestMixin to create a custom permission check.

# Real- Life Example
# Let's take the example of an article written by a certain author. We don't want any author to be able to modify it. Only its author will be able to do so:

# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']
#    def form_valid(self, form):
#         # Set the author to the current user
#         form.instance.author = self.request.user]
#         return super().form_valid(form)
#    def test_func(self):
#         post = self.get_object()
#         # Check if the current user is the author of the post
#           if self.request.user == post.author:
#             return True
#         else:
#             return False
# In this case, the test_func method checks if the current user is the author of the post. 
# If they are, they can update it. If not, they will be denied access.