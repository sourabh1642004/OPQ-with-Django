
from django.contrib import admin
from django.urls import path, include
from backendofOPQ import views
from feedback import views as fb
from quiz import views as qz


urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/<int:courseid>', views.Coursedetails),
    path('', views.indexpage,name="homepage"),
    path('newsdetails/<newsid>', views.newsDetails),
    path('feedback/', fb.feedbackfun,name="feedback"),
    path('quiz_start/',qz.quiz_start, name='quiz_start'),
    path('quiz_view/<int:quiz_id>/<int:question_number>/', qz.quiz_view, name='quiz_view'),
    path('quiz_view/<int:quiz_id>/', qz.quiz_view, name='quiz_view'),
    path('quiz_submission/<int:quiz_id>/',qz.quiz_submission, name='quiz_submission'),
    path('accounts/', include('useraccount.urls')),
]
