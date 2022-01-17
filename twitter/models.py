from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
from statistics import mode
from typing import Tuple
from django.db import models
from accounts.models import ProfileField

# Create your models here.
class Tweets(models.Model):
    tweet_text = models.CharField(max_length=280, blank=True, null=True, verbose_name='Tweet')
    image_tweet = models.ImageField(null=True, blank=True, verbose_name='Image')
    author = models.ForeignKey(ProfileField, on_delete=models.CASCADE, related_name='author', verbose_name='Author')
    posted_on = models.DateTimeField(auto_now_add=True, verbose_name='Posted on')
    
    class Meta:
        ordering = ['-posted_on']
    #comment

    def __str__(self):
        return self.tweet_text

class Retweet(models.Model):
    tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    retweeted_by = models.ForeignKey(ProfileField, on_delete=models.CASCADE)  

    def __str__(self):
        return str(self.tweet)        

class Comment(models.Model):
    comment_text = models.CharField(max_length=270, blank=False, verbose_name='Comment')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Commented on')
    comment_author = models.ForeignKey(ProfileField, on_delete=models.CASCADE, blank=False, null=True, related_name='commented_by', verbose_name='Commented by')
    tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE, blank=False, null=True)   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.comment_text     


class Like(models.Model):
    liked_user = models.ForeignKey(ProfileField, on_delete=models.CASCADE)
    liked_tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)

    def __str__(self):
        return self.liked_user
   

             