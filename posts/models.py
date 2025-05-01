from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Reverse is a function that returns the URL of a view by its name.

class Status(models.Model):
    """
    Model representing a status.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Post(models.Model):# We are two foreign key to the user model, which is a one-to-many relationship.
    """
    Model representing a post.
    """
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey( # ForeignKey make sure if the user is deleted, the post will be deleted too.
        get_user_model(), # This function returns the user model that is currently active in the project. It best practice not to hard code the user model.
        on_delete=models.CASCADE 
    )
    status = models.ForeignKey( # Foreign key make sure if the status is deleted, the post will be deleted too.
        Status, 
        on_delete=models.CASCADE # This means that if the status is deleted, all posts with that status will be deleted too.
    )
    created_on = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.id)])
    
