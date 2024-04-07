from django.shortcuts import render
from .models import feedback 


def feedbackfun(request):
    n=""
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        en=feedback(name=name, email=email, phone=phone, message=message)
        en.save()
        n="Data inserted"
    return render(request,"feedback.html", {'n': n})


# Create your views here.
