from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    header = models.CharField(max_length=50, null=False,)
    body = models.TextField(max_length=250, null=False,)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=False,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.header

    def get_upvote_url(self):
        return reverse('upvote', args=[self.id])

    def get_downvote_url(self):
        return reverse('downvote', args=[self.id])

class Votes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False,) 
    updated_at = models.DateTimeField(auto_now=True, null=False,) 

    def __str__(self):
        return self.user.username + ' ' + self.post.header + ' @ ' + str(self.created_at)