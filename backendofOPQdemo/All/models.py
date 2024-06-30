from django.db import models
from tinymce.models import HTMLField


class update(models.Model):
    date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100)
    # desc=HTMLField()
    desc=models.TextField(max_length=1000)
    # pdf=models.FileField(upload_to='pdfs/')
    

class feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=10)
    message=models.TextField()

def __str__(self):
    return self.name



