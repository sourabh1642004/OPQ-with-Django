from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.text
# Create your models here.
