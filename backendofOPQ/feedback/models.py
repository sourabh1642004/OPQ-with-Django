from django.db import models
class feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=10)
    message=models.TextField()

def __str__(self):
    return self.name

