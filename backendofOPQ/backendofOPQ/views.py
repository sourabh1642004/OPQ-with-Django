from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render

from django.shortcuts import render, redirect
from news.models import News



def indexpage(request):
    newData=News.objects.all();
    data={
        'newsData':newData
    }
    return render(request,"index.html",data)

def newsDetails(request,newsid):
    
    newsDetails=News.objects.get(id=newsid)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsdetails.html",data)


# def loginpage(request):
#     return render(request,"login.html")

def basepage(request):
    return render(request,"base.html")

def Coursedetails(request,courseid):
    return HttpResponse(courseid)

# def signuppage(request):
#     if request.method=="POST":
#         return HttpResponseRedirect()
    
#     return render(request,"signup.html")




