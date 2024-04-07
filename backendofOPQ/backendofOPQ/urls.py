
from django.contrib import admin
from django.urls import path
from backendofOPQ import views
from feedback import views as fb
from useraccount import views as ua
from quiz import views as qz


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ua.login, name="login"),
    path('course/<int:courseid>', views.Coursedetails),
    path('', views.indexpage),
    path('signup/',ua.signup, name="signup"),
    path('newsdetails/<newsid>', views.newsDetails),
    path('feedback/', fb.feedbackfun,name="feedback"),
    path('afterlogin/<int:user_id>/', ua.afterlogin, name="afterlogin"),
    path('quiz_start/',qz.quiz_start, name='quiz_start'),
    path('submit/',qz.quiz_submission, name='quiz_submission'),
    # path('quiz/',)
]
