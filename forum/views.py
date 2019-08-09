from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from forum.forms import SignUpForm
from .models import Topic, Post

def index(request):
    if request.user.is_authenticated:
        text_header = "Dashboard"
        text_paragraph = "Latest topics:" 
        topic_list = Topic.objects.order_by('-published_date')[:5]


        args = {'header': text_header, 'paragraph': text_paragraph, 'latest_topic_list': topic_list}

        #return render(request, 'forum/index.html', args)
         
    else:
        text_header = "Welcome in PyDJ Forum!"
        text_paragraph = "Please log in or create an account. xD"

        args = {'header': text_header, 
            'paragraph': text_paragraph}

    return render(request, 'forum/index.html', args)

def topicView(request, topic_id):
    if request.user.is_authenticated:
        topic = get_object_or_404(Topic, pk=topic_id)

        args = {'topic': topic}

    else:

        text_header = "Ups!"
        text_paragraph = "It seems that you are not logged in. If you want to see this page please authenticate. ;)"

        args = {'header': text_header, 
        'paragraph': text_paragraph}

    return render(request, 'forum/', args)

def allTopicsView(request, thread_id):
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