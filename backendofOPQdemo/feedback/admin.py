from django.contrib import admin

from .models import feedback

class feedbackAdmin(admin.ModelAdmin):
      list_display=('name','email','phone','message')

admin.site.register(feedback,feedbackAdmin)


# Register your models here.
