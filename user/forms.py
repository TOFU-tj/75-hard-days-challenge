from django import forms 
from user.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'email_field',
        'placeholder' : 'password_field',
    }))
    class Meta: 
        model = User 
        fields = {'email', 'password'}
        
    
