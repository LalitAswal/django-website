from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    return render(request, 'homepage/homepage.html')


def signup(request):
    if request.method == 'POST':
        # checking both password
        if request.POST['Password1'] == request.POST['Password2']:
            try:
                # checking user existence
                user = User.objects.get(username=request.POST['Username'])
                return render(request, 'homepage/Signup.html', {'error': 'User already exist '})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['Username'], password=request.POST['Password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'homepage/Signup.html', {'error': 'passwords  are  not same '})

    else:

        return render(request, 'homepage/Signup.html')


# login function
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['Username'], password=request.POST['Password1'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'homepage/login.html', {'error': 'username or password is incorrect'})
    else:

        return render(request, 'homepage/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
