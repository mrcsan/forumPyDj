from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
