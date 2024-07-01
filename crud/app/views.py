from django.shortcuts import redirect, render
from .models import UserModel

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Assuming you want to authenticate against UserModel
        try:
            user = UserModel.objects.get(name=username, password=password)
            return render(request, 'test.html')  # or redirect to a success page
        except UserModel.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        UserModel.objects.create(
            name=name,
            password=password,
            email=email,
        )
        
        return render(request, "login.html")
    else:
        return render(request, "signup.html")

def test(request):
    return render(request, 'test.html')
