from django.urls import path
from .views import Task

app_name = 'task_bar'

urlpatterns = [
    path('main_tasks_page/', Task.as_view(), name='main_tasks'),
    
]
