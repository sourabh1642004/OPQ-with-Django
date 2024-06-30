from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from django.shortcuts import render, redirect
from All.models import update

#define time range
time_threshold = timezone.now() - timedelta(days=7)

def indexpage(request):
    
    updatedata=update.objects.order_by('date')[0:3]
    # updatedata=update.objects.all()
    
    updatedata={
        'updatedata':updatedata
    }
    return render(request,"index.html",updatedata)

def updatedetails(request,updateid):
    
    updatedetails=update.objects.get(id=updateid)
    data={
        'updatedetails':updatedetails
    }
    return render(request,"updatedetails.html",data)


# def loginpage(request):
#     return render(request,"login.html")

# def basepage(request):
#     return render(request,"base.html")

# def Coursedetails(request,courseid):
#     return HttpResponse(courseid)

# def signuppage(request):
#     if request.method=="POST":
#         return HttpResponseRedirect()
    
#     return render(request,"signup.html")




