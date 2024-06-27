from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=('date','title','desc','pdf')
    
    
admin.site.register(News,NewsAdmin)

