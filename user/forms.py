from django import forms 
from user.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email',
            'type': 'email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )
    class Meta: 
        model = User 
        fields = {'email', 'password'}
        
    
class UserRegistrationForm(UserCreationForm): 
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Введите имя пользователя'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email', 
            'type': 'email'
        })
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Введите пароль'
        })
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Повторите пароль'
        })
    )
    weight = forms.IntegerField(
        label='Вес (кг)',
        widget=forms.NumberInput(attrs={
            'class': 'input-box',
            'placeholder': 'Введите ваш вес'
        })
    )
    height = forms.IntegerField(
        label='Рост (см)',
        widget=forms.NumberInput(attrs={
            'class': 'input-box',
            'placeholder': 'Введите ваш рост'
        })
    )
    age = forms.IntegerField(
        label='Возраст',
        widget=forms.NumberInput(attrs={
            'class': 'input-box',
            'placeholder': 'Введите ваш возраст'
        })
    )
    
    class Meta: 
        model = User
        fields = {'username', 'password1', 'password2', 'email', 'weight', 'height', 'age', }