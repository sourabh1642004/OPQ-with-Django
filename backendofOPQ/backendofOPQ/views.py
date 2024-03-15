from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect



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




def loginpage(request):
    return render(request,"login.html")

def basepage(request):
    return render(request,"base.html")

def Coursedetails(request,courseid):
    return HttpResponse(courseid)




def register_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            phone_number=phone_number,
            address=address
        )
        # Redirect to a success page or another URL
        return redirect('success_page')  # Replace 'success_page' with the appropriate URL name
    else:
        return render(request, 'student_registration.html')



