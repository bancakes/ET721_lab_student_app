from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[('academic', 'Academic'), ('personal', 'Personal')])
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
