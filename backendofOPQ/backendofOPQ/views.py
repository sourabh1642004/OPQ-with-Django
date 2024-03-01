from django.http import HttpResponse
from django.shortcuts import render




def indexpage(request):
    data={
        'title':'Welcome',
        'bdata':'welcome sourabh',
        'clist':['php','java','django'],
        'student_details':[
            {'name':'pradeep','phone' : 7976890679},
            {'name':'testing','phone': 9982148469}
        ]
    }
    return render(request,"index.html")




def aboutus(request):
    return HttpResponse("welcome to onlineportal")

def Coursedetails(request,courseid):
    return HttpResponse(courseid)