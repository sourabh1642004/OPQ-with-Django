from django.db import models
from tinymce.models import HTMLField
class News(models.Model):
    date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100)
    desc=HTMLField()
    pdf=models.FileField(upload_to='pdfs/')
    



    