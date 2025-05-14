from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView, TemplateView
from task_bar.models import Task, ArchivedTask
from task_bar.forms import TasksForm
from django.http import JsonResponse, HttpResponseBadRequest, Http404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@require_POST
@login_required
def toggle_task_field(request, task_id, field):
    try:
        task = Task.objects.get(pk=task_id, user=request.user)
        if hasattr(task, field):
            current_value = getattr(task, field)
            setattr(task, field, not current_value)
            task.check_completion()
            task.save()
            return JsonResponse({'success': True, 'new_value': not current_value})
        else:
            return HttpResponseBadRequest("Неверное поле")
    except Task.DoesNotExist:
        return HttpResponseBadRequest("Задача не найдена")



# task_bar/views.py

from django.shortcuts import redirect

class TasksUpdateView(UpdateView):
    model = Task
    form_class = TasksForm
    template_name = "task_bar/task_update.html"

    def get_object(self, queryset=None):
        day = self.kwargs.get('day')
        current_day = self.request.user.current_day or 1

        if day != current_day:
            raise Http404("Вы можете редактировать только текущий день")

        task, _ = Task.objects.get_or_create(
            user=self.request.user,
            day=day
        )
        return task

    def form_valid(self, form):
        response = super().form_valid(form)
        task = form.instance

        # Проверим, завершён ли день
        task.check_completion()

        # Если задача полностью завершена — отправим на success.html
        if task.completed:
            return redirect('task_bar:success')

        return response




class SuccessView(TemplateView):
    template_name = "task_bar/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        archived_tasks = ArchivedTask.objects.filter(user=self.request.user)

        context['archived_tasks'] = archived_tasks
        return context
    
    



class TaskListView(ListView):
    model = ArchivedTask
    template_name = "task_bar/tasks_demo.html"

     
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_day = self.request.user.current_day or 1
        days_list = []

        for day in range(1, 76):  
            task = context['object_list'].filter(day=day).first()
            days_list.append({  
                'day': day,
                'task': task,
                'exists': bool(task),
            })

        context['days_list'] = days_list
        context['current_day'] = current_day
        return context

