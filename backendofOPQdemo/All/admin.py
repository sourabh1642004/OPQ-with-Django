from django.contrib import admin
from .models import update,feedback

class updateAdmin(admin.ModelAdmin):
    list_display=('date','title','desc')
    
    
admin.site.register(update,updateAdmin)

class feedbackAdmin(admin.ModelAdmin):
      list_display=('name','email','phone','message')

admin.site.register(feedback,feedbackAdmin)





