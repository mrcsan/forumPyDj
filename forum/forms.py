from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Thread

class PostForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('thread_title', 'thread_text',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LogInForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=False)
    password = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'password',)