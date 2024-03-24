
from django.contrib import admin
from django.urls import path
from backendofOPQ import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginpage),
    path('course/<int:courseid>', views.Coursedetails),
    path('', views.indexpage),
    path('signup/',views.signuppage),
    path('newsdetails/<newsid>', views.newsDetails),
]
