from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Registration view
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # After successful registration

# Custom Password Change view
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    
    # Redirect to the homepage after password change
    def get_success_url(self):
        return reverse_lazy('home')  # Redirect to the homepage after password change