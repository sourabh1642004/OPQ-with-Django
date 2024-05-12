from django.contrib import admin
from .models import Quiz,Question,Choice

class QuizAdmin(admin.ModelAdmin):
    list_display=('title',)

class QuestionAdmin(admin.ModelAdmin):
    list_display=('quiz','text')
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display=('question','text','is_correct')

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)