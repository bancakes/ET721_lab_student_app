from django.db import models

# Define a model for image uploads
class NoteImage(models.Model):
    subject_choices = [
        ('math', 'Math'),
        ('science', 'Science'),
        ('history', 'History'),
        ('english', 'English'),
        ('other', 'Other')
    ]
    
    image = models.ImageField(upload_to='notes/images/')
    subject = models.CharField(max_length=20, choices=subject_choices, default='other')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded for {self.subject} at {self.uploaded_at}"
