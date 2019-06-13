from django.contrib import admin

from .models import Topic
from .models import Post

admin.site.register(Topic)
admin.site.register(Post)
