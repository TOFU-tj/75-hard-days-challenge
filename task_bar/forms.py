from django import forms
from task_bar.models import Task

class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'drank_water',
            'workout_1',
            'workout_2',
            'read_pages',
            'no_junk_food',
            'no_alcohol',
            'progress_photo'
        ]
