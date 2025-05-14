from django.urls import path
from user.views import UserLoginView, UserRegistrationsView
from . import views
app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegistrationsView.as_view(), name='register'),
    path('logout', views.logout, name='logout')
]
