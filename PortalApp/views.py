from django.shortcuts import render, redirect
from .models import Score
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def portal(request):
    user = request.user
    score = Score.objects.filter(user=user)
    context = {"scores": score}
    return render(request, 'portal.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have Successfully Logged In !!')
            return redirect('portal')
        else:
            messages.error(request, "Invalid username or password !!!") 
    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, 'You have Successfully Logged Out!!')
    return redirect('index')