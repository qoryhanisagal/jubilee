from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Aut-login after registration
            
            messages.success(request, "Your account was created successfully! Welcome to Jubilee.") # Send a success message

            return redirect('home')  # After successful registeration, redirect to home
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form}) # This is the registration view
