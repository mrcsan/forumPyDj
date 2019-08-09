from django.shortcuts import render, redirect
from django.http import HttpResponse
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

def threadView(request, thread_id):
    if request.user.is_authenticated:
        thread_title = thread_id
        post_list = Post.objects.order_by('-published_date')[:5]

        args = {'header': thread_title, 'paragraph': text_paragraph, 'latest_post_list': post_list}

    else:   
        text_header = "Ups!"
        text_paragraph = "It seems that you are not logged in. If you want to see this page please authenticate. ;)"

        args = {'header': text_header, 
        'paragraph': text_paragraph}

    return render(request, 'forum/thread.html', args)

def allThreadsView(request, thread_id):
    return 

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
            return redirect('index')
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

def dashboardView(request):
    text_header = "Dashboard"
    text_paragraph = "This is content" 
    topic_list = Topic.objects.order_by('-published_date')[:5]
    post_list = Post.objects.order_by('-published_date')[:5]
    #output = ', '.join([t.thread_title for t in latest_threads_list])

    args = {'header': text_header, 'paragraph': text_paragraph, 'latest_topic_list': topic_list, 'latest_post_list': post_list}

    return  render(request, 'forum/dashboard.html', args)