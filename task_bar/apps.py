from django.apps import AppConfig


class TaskBarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_bar'

    def ready(self):
        import task_bar.signals 