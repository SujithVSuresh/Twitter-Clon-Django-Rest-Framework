from django.shortcuts import render, get_object_or_404
from rest_framework import generics, request, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from twitter.serializers import TweetSerializer, CommentSerializer, LikeSerializer, RetweetSerializer
from .models import Comment, Tweets, Like, Retweet
from accounts.models import ProfileField, FollowUnfollow

# Create your views here.
class TweetView(generics.ListCreateAPIView): 
    #queryset = Tweets.objects.all() 
    serializer_class = TweetSerializer 

    def get_queryset(self):
        self.myprof = get_object_or_404(ProfileField, user_name=self.request.user.id) 
        self.myfollow = FollowUnfollow.objects.get(main_user=self.myprof)
        self.myfollowing = self.myfollow.following.all()
        return Tweets.objects.filter(author__in=self.myfollowing)    

    def perform_create(self, serializer):
        self.author = ProfileField.objects.get(user_name=self.request.user)
        serializer.save(author=self.author) 

class TweetDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Tweets.objects.all() 
    serializer_class = TweetSerializer  

class CommentView(generics.ListCreateAPIView): 
    #queryset = Comment.objects.all() 
    serializer_class = CommentSerializer  
    def get_queryset(self):
        self.tweet = get_object_or_404(Tweets, id=self.kwargs['pk'])
        return Comment.objects.filter(tweet=self.tweet)

    def perform_create(self, serializer):
        self.tweet = get_object_or_404(Tweets, id=self.kwargs['pk'])
        self.author = ProfileField.objects.get(user_name=self.request.user)
        serializer.save(comment_author=self.author, tweet=self.tweet)    

class LikeView(generics.ListCreateAPIView, mixins.DestroyModelMixin): 
    serializer_class = LikeSerializer 

    def get_queryset(self):
        self.tweet = get_object_or_404(Tweets, id=self.kwargs['pk'])
        return Like.objects.filter(liked_tweet=self.tweet)

    def perform_create(self, serializer):
        self.tweet = get_object_or_404(Tweets, id=self.kwargs['pk'])
        self.userprofile = ProfileField.objects.get(user_name=self.request.user)
        if Like.objects.filter(liked_user=self.userprofile, liked_tweet=self.tweet).exists():
            raise ValidationError('You have already liked this post')
        serializer.save(liked_user=self.userprofile, liked_tweet=self.tweet)         

    def delete(self, request, *args, **kwargs):
        self.tweet = get_object_or_404(Tweets, id=self.kwargs['pk'])
        self.userprofile = ProfileField.objects.get(user_name=self.request.user)
        like_check = Like.objects.filter(liked_user=self.userprofile, liked_tweet=self.tweet)
        if like_check.exists():
            like_check.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted this post')    

class RetweetView(generics.ListCreateAPIView): 
    serializer_class =  RetweetSerializer

    def get_queryset(self):
        self.tweet = get_object_or_404(Tweets, id=self.kwargs['pk'])
        return Retweet.objects.filter(tweet=self.tweet)
    
    def perform_create(self, serializer):
        self.tweet = get_object_or_404(Tweets, id=self.kwargs['pk'])
        self.userprofile = ProfileField.objects.get(user_name=self.request.user)
        if Retweet.objects.filter(tweet=self.tweet, retweeted_by=self.userprofile):
            raise ValidationError('You have already retweeted this post')
        serializer.save(retweeted_by=self.userprofile, tweet=self.tweet) 
              
            