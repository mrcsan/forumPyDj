from django import forms

from .models import Post
from .models import Thread

class PostForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('thread_title', 'thread_text',)