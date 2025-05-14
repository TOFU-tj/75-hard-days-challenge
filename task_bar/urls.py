from django.urls import path
from .views import TaskListView, TasksUpdateView, SuccessView
from . import views
app_name = 'task_bar'


urlpatterns = [
    path('main_tasks_page/', TaskListView.as_view(), name='task-list'),
    path('update/<int:day>/', TasksUpdateView.as_view(), name='task-update'),
    path('<int:task_id>/<str:field>/toggle/', views.toggle_task_field, name='toggle-task-field'),
    path('success/', SuccessView.as_view(), name='success'),
]
    
