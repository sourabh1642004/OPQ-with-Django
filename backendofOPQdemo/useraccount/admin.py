from django.contrib import admin
from .models import User

class userAdmin(admin.ModelAdmin):
      list_display=('first_name','last_name','email','password')

admin.site.register(User,userAdmin)


# Register your models here.
