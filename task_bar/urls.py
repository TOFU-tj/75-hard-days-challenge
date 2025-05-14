from django.urls import path
from .views import TaskListView, TasksUpdateView

app_name = 'task_bar'


urlpatterns = [
    path('main_tasks_page/', TaskListView.as_view(), name='task-list'),
    path('update/<int:pk>/', TasksUpdateView.as_view(), name='task-update'),
]
    
