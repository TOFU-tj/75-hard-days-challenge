from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    
    challenge_started = models.DateTimeField(auto_now=True, null=True, blank=True)
    current_day = models.PositiveIntegerField(default=1)
    last_checked = models.DateField(default=timezone.now)
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username





   