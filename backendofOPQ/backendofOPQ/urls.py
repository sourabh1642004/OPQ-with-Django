
from django.contrib import admin
from django.urls import path
from backendofOPQ import views
from feedback import views as fb


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginpage),
    path('course/<int:courseid>', views.Coursedetails),
    path('', views.indexpage),
    path('signup/',views.signuppage),
    path('newsdetails/<newsid>', views.newsDetails),
    path('feedback/', fb.feedbackfun,name="feedback"),
]
