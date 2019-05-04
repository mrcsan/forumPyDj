from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from forum.forms import SignUpForm
from forum.forms import LogInForm


def index(request):
    text_header = "Welcome in PyDJ Forum!"
    text_paragraph = "Please log in or create an account. xD"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/index.html', args)

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
    text_header = "You have logged in as "
    text_paragraph = "Content on this site will be available in the future. xD"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/logedin.html', args)

def login(request):
    text_header = "Login"
    text_paragraph = "You can login here!"

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = LogInForm()
    return render(request, 'forum/login.html', {'form': form, 'header': text_header, 'paragraph': text_paragraph})

def logout(request):
    text_header = "You have logged out!"
    text_paragraph = "See you later. :D"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/logout.html', args)