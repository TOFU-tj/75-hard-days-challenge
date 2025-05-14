from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from user.models import User
from user.forms import UserLoginForm, UserCreationForm, UserRegistrationForm
from django.views.generic import CreateView



class UserLoginView(LoginView): 
    template_name = "user/login.html"
    form_class = UserLoginForm
    
    def get_success_url(self): 
        return reverse('task_bar:task-list')
    

class UserRegistrationsView(CreateView): 
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:user_login')
    
    
