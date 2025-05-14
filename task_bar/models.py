# from django.db import models
# from user.models import User
# from django.urls import reverse



# class Task(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')
#     day = models.PositiveIntegerField()

#     drank_water = models.BooleanField(default=False)
#     workout_1 = models.BooleanField(default=False)
#     workout_2 = models.BooleanField(default=False)
#     read_pages = models.BooleanField(default=False)
#     no_junk_food = models.BooleanField(default=False)
#     no_alcohol = models.BooleanField(default=False)
#     progress_photo = models.BooleanField(default=False)
#     completed = models.BooleanField(default=False)

#     # def check_completion(self):
#     #     fields = [
#     #         self.drank_water,
#     #         self.workout_1,
#     #         self.workout_2,
#     #         self.read_pages,
#     #         self.no_junk_food,
#     #         self.no_alcohol,
#     #         self.progress_photo
#     #     ]
#     #     if all(fields):
#     #         self.completed = True
#     #         self.save(update_fields=['completed'])

           
#     #         if self.user.current_day < 75:
#     #             self.user.current_day += 1
#     #             self.user.save()
                

#     #         Task.objects.get_or_create(user=self.user, day=self.user.current_day)

#     def check_completion(self):
#         fields = [
#             self.drank_water,
#             self.workout_1,
#             self.workout_2,
#             self.read_pages,
#             self.no_junk_food,
#             self.no_alcohol,
#             self.progress_photo
#         ]
#         if all(fields):
#             self.completed = True
#             self.save(update_fields=['completed'])

#             if self.user.current_day == 1:
#                 # Архивируем как JSON
#                 data = {
#                     "drank_water": self.drank_water,
#                     "workout_1": self.workout_1,
#                     "workout_2": self.workout_2,
#                     "read_pages": self.read_pages,
#                     "no_junk_food": self.no_junk_food,
#                     "no_alcohol": self.no_alcohol,
#                     "progress_photo": self.progress_photo,
#                     "completed": self.completed,
#                 }
#                 ArchivedTask.objects.create(user=self.user, day=self.day, data=data)
#                 self.delete()

#             if self.user.current_day < 75:
#                 self.user.current_day += 1
#                 self.user.save()

#             Task.objects.get_or_create(user=self.user, day=self.user.current_day)


#     def get_absolute_url(self):
#         return reverse("task_bar:task-list")

#     class Meta:
#         verbose_name = "Задача"
#         verbose_name_plural = "Задачи"
#         unique_together = ('user', 'day')  

#     def __str__(self):
#         return f"День {self.day} — {self.user.username}"
    
    
# class ArchivedTask(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='archived_tasks')
#     day = models.PositiveIntegerField()
#     data = models.JSONField()

#     from .models import ArchivedTask

#     class Meta:
#         unique_together = ('user', 'day')



from django.db import models
from user.models import User
from django.urls import reverse


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    day = models.PositiveIntegerField()

    drank_water = models.BooleanField(default=False)
    workout_1 = models.BooleanField(default=False)
    workout_2 = models.BooleanField(default=False)
    read_pages = models.BooleanField(default=False)
    no_junk_food = models.BooleanField(default=False)
    no_alcohol = models.BooleanField(default=False)
    progress_photo = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def check_completion(self):
        fields = [
            self.drank_water,
            self.workout_1,
            self.workout_2,
            self.read_pages,
            self.no_junk_food,
            self.no_alcohol,
            self.progress_photo
        ]
        if all(fields):
            self.completed = True
            self.save(update_fields=['completed'])

            if self.user.current_day == 1:
                # Архивируем как JSON
                data = {
                    "drank_water": self.drank_water,
                    "workout_1": self.workout_1,
                    "workout_2": self.workout_2,
                    "read_pages": self.read_pages,
                    "no_junk_food": self.no_junk_food,
                    "no_alcohol": self.no_alcohol,
                    "progress_photo": self.progress_photo,
                    "completed": self.completed,
                }
                ArchivedTask.objects.create(user=self.user, day=self.day, data=data)
                self.delete()

            if self.user.current_day < 75:
                self.user.current_day += 1
                self.user.save()

            Task.objects.get_or_create(user=self.user, day=self.user.current_day)

    def get_absolute_url(self):
        return reverse("task_bar:task-list")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        unique_together = ('user', 'day')

    def __str__(self):
        return f"День {self.day} — {self.user.username}"


class ArchivedTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='archived_tasks')
    day = models.PositiveIntegerField()
    data = models.JSONField()

    class Meta:
        unique_together = ('user', 'day')

    def __str__(self):
        return f"Архив: День {self.day} — {self.user.username}"
