
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import HttpResponse,HttpResponseRedirect
from .models import User

def signup(request):
    n="fill the all details"
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('femail')
        confirm_email = request.POST.get('semail')
        password = request.POST.get('password')
        confirm_password = request.POST.get('spassword')
       
        if email !=  confirm_email:
           return render(request, 'signup.html',{'error_email': 'email do not match'})
        if password != confirm_password:
            return render(request, 'signup.html', {'error_password': 'Passwords do not match'})
        
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, "signup.html",{'n':n})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('femail')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email, password=password)
            #add if else statement
            
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')

