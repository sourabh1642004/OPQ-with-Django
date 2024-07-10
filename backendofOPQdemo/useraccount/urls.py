from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/<int:user_id>/',views.edit_profile, name='editprofile'),
    path('signup/', views.signup, name="signup"),
    path('afterlogin/<int:user_id>/', views.afterlogin, name="afterlogin"),
    path('forgetpassword/', views.forgetpassword , name='forgetpassword'),
    path('changepassword/<int:user_id>/', views.changepassword, name='changepassword'),
]