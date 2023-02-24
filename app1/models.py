from django.db import models

# Create your models here.
class Flick(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    tags = models.CharField(max_length=300)
    picture = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    