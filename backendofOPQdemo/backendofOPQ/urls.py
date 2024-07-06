
from django.contrib import admin
from django.urls import path, include
from backendofOPQ import views
from quiz import views as qz
from All import views as fb

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('course/<int:courseid>', views.Coursedetails),
    path('', views.indexpage,name="homepage"),
    path('updatedetails/<updateid>', views.updatedetails),
    path('feedback/', fb.feedbackfun,name="feedback"),
    path('quiz_start/<int:user_id>',qz.quiz_start, name='quiz_start'),
    path('quiz_view/<int:user_id>/<int:quiz_id>/<int:question_number>', qz.quiz_view, name='quiz_view'),
    path('quiz_view/<int:user_id>/<int:quiz_id>', qz.quiz_view, name='quiz_view'),
    path('quiz_submission/<int:user_id>/<int:quiz_id>',qz.quiz_submission, name='quiz_submission'),
    path('accounts/', include('useraccount.urls')),
    path('allupdate/',fb.allupdates)
]
