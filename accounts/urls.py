from django.urls import path
from .views import SignUpView, CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='signup'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]