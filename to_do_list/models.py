from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('personal', 'Personal'),
        ('deadline', 'Deadline'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Optional field
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    due_date = models.DateTimeField(blank=True, null=True)  # Optional due date
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
