
from .models import UserModel
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
         

        # Authenticate user
        try:
            user = UserModel.objects.get(name=username)
            if user.check_password(password):
                return render(request, 'profileEdit.html', {'user': user})  # or redirect to a success page
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        except UserModel.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        image=request.POST.get(request.FILES.get('images'))
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = UserModel(name=name, email=email)
        user.set_password(password)  # Hash the password before saving
        user.save()

        return render(request, "login.html")
    else:
        return render(request, "signup.html")

def logout(request):
    return render(request, 'index.html')




def profileCreate(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        umail = request.POST.get('email')
        pwd = request.POST.get('password')


        user = UserModel.objects.create(name=uname, email=umail, password=pwd)  # Hash the password in a real application
        user.save()
 

    return render(request, 'profileEdit.html')



def profileEdit(request, pk):
    user = get_object_or_404(UserModel, pk=pk)

    if request.method == 'POST':
        uname = request.POST.get('name')
        umail = request.POST.get('email')
        pwd= request.POST.get('password')

        if not (uname and umail and pwd):
            return render(request, 'profileEdit.html', {'user': user})
        
        user.name = uname
        user.email = umail  # In a real scenario, hash the password
        user.password=pwd
        user.save()
        # return render(request, "profileEdit.html", {'user': user})
        return redirect('profileEdit', pk=user.pk)

    return render(request, "profileEdit.html", {'user': user})


