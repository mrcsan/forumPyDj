from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from forum.forms import SignUpForm


def index(request):
    text_header = "Welcome in PyDJ Forum!"
    text_paragraph = "Please log in or create an account. xD"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/index.html', args)

def threadView(request, thread_id):

    text_header = "Ups!"
    text_paragraph = "It seems that you are not logged in. If you want to see this page please authenticate. ;)"

    return HttpResponse("You're looking at thread %s." % thread_id)

def allThreadsView(request, thread_id):
    return HttpResponse("You're looking at thread %s." % thread_id)

#def allPostsView(request, thread_id):
    #return HttpResponse("You're looking at thread %s." % thread_id)

def registrationView(request):
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

def logedinView(request):
    current_username = request.user.username
    text_header = "You have logged in as "
    text_paragraph = "Content on this site will be available in the future. xD"

    args = {'header': text_header, 
            'paragraph': text_paragraph,
            'username': current_username,}
    return render(request, 'forum/logedin.html', args)

def loginView(request):
    text_header = "Login"
    text_paragraph = "You can login here!"
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('logedin')
    else:
        form = AuthenticationForm()
    return render(request, 'forum/login.html', {'form': form, 'header': text_header, 'paragraph': text_paragraph})

def logoutView(request):
    logout(request)
    text_header = "You have logged out!"
    text_paragraph = "See you later. :D"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/logout.html', args)

def faqView(request):
    text_header = "FAQ - Frequently asked questions"
    text_paragraph = "Content on this site will be available in the future. xD"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/faq.html', args)