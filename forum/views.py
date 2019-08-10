from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from forum.forms import SignUpForm
from .models import Topic, Post
from django.http import HttpResponse

def index(request):
    if request.user.is_authenticated:
        logged_user_name = request.user.username
        text_header = "Welcome in your dashboard " + logged_user_name + " ;D"
        text_paragraph = "Here are the latest topics on forum:" 
        topic_list = Topic.objects.order_by('-published_date')[:5]

        args = {'header': text_header, 'paragraph': text_paragraph, 'latest_topic_list': topic_list}
         
    else:
        text_header = "Welcome in PyDJ Forum!"
        text_paragraph = "Please log in or create an account. xD"

        args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/index.html', args)

def topicView(request, topic_id):
    if request.user.is_authenticated:

        # text_header = "You're looking at topic %s." % topic_id
        # text_paragraph = "You're looking at topic %s." % topic_id

        text_header = Topic.topic_title
        text_paragraph = Topic.topic_text

        args = {'header': text_header, 'paragraph': text_paragraph}

    else:
        text_header = "Ups!"
        text_paragraph = "It seems that you are not logged in. If you want to see this page please authenticate. ;)"

        args = {'header': text_header, 'paragraph': text_paragraph}

    return render(request, 'forum/topic_view.html', args)

def allTopicsView(request, topic_id):
    return 

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
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'forum/registration.html', {'form': form})

def loginView(request):
    text_header = "Login"
    text_paragraph = "You can login here!"
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'forum/login.html', {'form': form, 'header': text_header, 'paragraph': text_paragraph})

def logoutView(request):
    logout(request)
    text_header = "You have logged out!"
    text_paragraph = "See you later. :D"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/index.html', args)

def faqView(request):
    text_header = "FAQ - Frequently asked questions"
    text_paragraph = "Content on this site will be available in the future. xD"

    args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/faq.html', args)