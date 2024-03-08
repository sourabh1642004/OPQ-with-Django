
from django.contrib import admin
from django.urls import path
from backendofOPQ import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginpage),
    path('base/', views.basepage),
    path('course/<int:courseid>', views.Coursedetails),
    path('', views.indexpage),
]


from django.urls import path
from .views import register_student

urlpatterns = [
    path('register/', register_student, name='register_student'),
    # Add other URL patterns if needed
]