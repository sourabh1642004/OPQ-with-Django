from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    # select_list=models.CharField(max_length=10)
    
    

# Create your models here.