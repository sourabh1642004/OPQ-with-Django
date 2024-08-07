from django.contrib.auth import authenticate, login as auth_login

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import HttpResponse,HttpResponseRedirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
import random
import string
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
           return render(request, 'signup.html',{'n': 'email do not match'})
        if password != confirm_password:
            return render(request, 'signup.html', {'n': 'Passwords do not match'})
        
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, "signup.html",{'n':n})

def login(request):
    n=""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email, password=password)
            
            
            return redirect('afterlogin',user_id=user.id)

        except User.DoesNotExist:
            return render(request, 'login.html', {'n': 'Invalid email or password'})
    
    return render(request, 'login.html',{'n':n})

def afterlogin(request,user_id):
    try:
        user=User.objects.get(id=user_id)
        return render(request,'afterlogin.html',{'user':user})
    except User.DoesNotExist:
        return redirect('login')

def profile(request,user_id):
    # if 'user_id' not in request.session:
    #     return redirect('login')

    # user = User.objects.get(id=request.session['user_id'])
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})

def edit_profile(request,user_id):
    # if 'user_id' not in request.session:
    #     return redirect('login')

    # user = User.objects.get(id=request.session['user_id'])
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        # user.bio = request.POST.get('bio')
        # user.phone = request.POST.get('phone')
        user.save()
        return redirect('profile',user_id=user_id)

    return render(request, 'edit_profile.html', {'user': user})
    
    


def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Generate a mixed password: 8 characters long, including letters and digits
        characters = string.ascii_letters + string.digits
        mixed_password = ''.join(random.choice(characters) for i in range(8))

        try:
            user = User.objects.get(email=email)
            subject = f"Password Reset Request for {user.first_name}"
            message = (
                f"Dear {user.first_name},\n\n"
                "Your request to reset your password has been approved. "
                "Please find your new password below. We strongly recommend "
                "changing this password immediately after logging in.\n\n"
                f"New Password: {mixed_password}\n\n"
                "If you did not request a password reset, please ignore this email or contact support.\n\n"
                "Best,\nThe Team Of OPQ"
            )
            send_mail(subject, message, "sourabh1642004@gmail.com", [email])
            user.password=mixed_password  # Use set_password to properly hash the password
            user.save()
            return render(request, 'forgetpassword.html', {'message': 'Password reset email has been sent.'})
        except User.DoesNotExist:
            return render(request, 'forgetpassword.html', {'message': 'Email does not exist.'})

    return render(request, 'forgetpassword.html')



def changepassword(request,user_id):
    user=User.objects.get(id=user_id)
    if request.method == 'POST':
        password=request.POST.get('password')
        confirm_password=request.POST.get('spassword')
        if password==confirm_password:
            user.password=password
            user.save()
            return redirect('login')
        else:
            return render(request,'changepassword.html',{'message':'password does not match.'})
    
    return render(request,'changepassword.html',{'user_id':user.id})

   
   
