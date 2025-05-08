from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    test_403_view,
    DraftPostListView,  
    ArchivedPostListView
)

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('drafts/', DraftPostListView.as_view(), name='post_drafts'), 
    path('archived/', ArchivedPostListView.as_view(), name='post_archived'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('forbidden/', test_403_view, name='forbidden'),    
]
