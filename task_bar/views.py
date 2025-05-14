from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from task_bar.models import Task
from task_bar.forms import TasksForm


class TasksUpdateView(UpdateView): 
    model = Task
    form_class = TasksForm
    template_name = "task_bar/task_update.html"
    

class TaskListView(ListView):
    model = Task
    template_name = "task_bar/tasks_demo.html"
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    

