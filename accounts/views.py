from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'accounts/login.html')


@login_required
def logout_page(request):
    auth.logout(request)
    return redirect('login')


