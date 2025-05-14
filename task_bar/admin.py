from django.contrib import admin
from task_bar.models import Task, ArchivedTask

admin.site.register(Task)
admin.site.register(ArchivedTask)
# Register your models here.
