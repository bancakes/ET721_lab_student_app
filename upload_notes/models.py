from django.db import models

# Create your models here.
class NoteImage(models.Model):
    subject = models.CharField(max_length=100)
    image = models.ImageField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
