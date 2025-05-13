from django.shortcuts import render
from django.views.generic import TemplateView



class Task(TemplateView): 
    template_name = 'task_bar/tasks.html'