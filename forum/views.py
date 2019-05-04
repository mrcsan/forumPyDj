from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from forum.forms import SignUpForm
from forum.forms import LogInForm


def index(request):
    #return HttpResponse("Hello, world. You're at the forum index.")
    return render(request, 'forum/index.html', {})

def detail(request, thread_id):
    return HttpResponse("You're looking at thread %s." % thread_id)

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print("email: "+str(form.cleaned_data.get('email')))
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('logedin')
    else:
        form = SignUpForm()
    return render(request, 'forum/registration.html', {'form': form})

def logedin(request):
    return render(request, 'forum/logedin.html', {})

def login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('logedin')
    else:
        form = LogInForm()
    return render(request, 'forum/login.html', {'form': form})

def logout(request):
    return render(request, 'forum/logout.html', {})