from django.db import models
from user.models import User
from django.urls import reverse

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.PositiveIntegerField()  

    drank_water = models.BooleanField(default=False)
    workout_1 = models.BooleanField(default=False)
    workout_2 = models.BooleanField(default=False)
    read_pages = models.BooleanField(default=False)
    is_day_completed = models.BooleanField(default=False)
    no_junk_food = models.BooleanField(default=False)
    no_alcohol = models.BooleanField(default=False)
    progress_photo = models.BooleanField(default=False)
    
    
    def check_completion(self):
        fields = [
            self.drank_water,
            self.workout_1,
            self.workout_2,
            self.no_junk_food,
            self.no_alcohol,
            self.read_pages,
            self.progress_photo
        ]
        self.completed = all(fields)
        self.save()
        
    def get_absolute_url(self):
        return reverse("task_bar:task-list")
    

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        unique_together = ('user', 'day')  

    def __str__(self):
        return f"Day {self.day} — {self.user.username}"

def create_tasks_for_user(user):
    for day in range(1, 76):  # Days 1 to 75
        Task.objects.get_or_create(user=user, day=day)


