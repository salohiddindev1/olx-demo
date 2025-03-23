from django.shortcuts import render
from users.models import User

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        data = request.POST
        phone = data.get('phone')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(phone_number=phone).exists():
                return render(request, 'login.html', {'message': 'Phone number already exists'})
            else:
                user = User.objects.create_user(phone_number=phone, password=password, username=phone)
                user.save()
                return render(request, 'login.html', {'message': 'Registration successful'})
        else:
            return render(request, 'login.html', {'message': 'Passwords do not match'})
        
    return render(request, 'index.html')

def profile_view(request):
    return render(request, 'profile.html')