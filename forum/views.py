from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the forum index.")

def detail(request, thread_id):
    return HttpResponse("You're looking at thread %s." % thread_id)

def registration(request):
    return HttpResponse("You're looking at registration site.")

def login (request):
    return HttpResponse("You're looking at login site.")