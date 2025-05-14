# task_bar/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Task

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_initial_tasks(sender, instance, created, **kwargs):
    if created:
        tasks = [Task(user=instance, day=d) for d in range(1, 76)]
        Task.objects.bulk_create(tasks)