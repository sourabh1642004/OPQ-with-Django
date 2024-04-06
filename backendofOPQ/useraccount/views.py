
from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email, password=password)
            # Handle login success
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')
# Create your views here.
