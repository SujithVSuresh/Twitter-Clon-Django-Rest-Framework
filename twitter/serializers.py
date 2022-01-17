from rest_framework import serializers
from .models import Tweets, Comment, Like, Retweet

class TweetSerializer(serializers.ModelSerializer):
    commentcount = serializers.SerializerMethodField()
    likecount = serializers.SerializerMethodField() 
    retweetcount = serializers.SerializerMethodField()
    class Meta:
        model = Tweets
        fields = ('id', 'tweet_text', 'image_tweet', 'author', 'posted_on', 'likecount', 'commentcount', 'retweetcount')
        read_only_fields = ('posted_on', 'author', 'likecount', 'commentcount', 'retweetcount')

    def get_commentcount(self, pk):
        return Comment.objects.filter(tweet=pk).count() 

    def get_likecount(self, pk):
        return  Like.objects.filter(liked_tweet=pk).count()   

    def get_retweetcount(self, pk):
        return  Retweet.objects.filter(tweet=pk).count()       

     

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'tweet', 'comment_text', 'comment_author', 'created_on')
        read_only_fields = ('created_on', 'comment_author', 'tweet',)   

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'liked_user')
        read_only_fields = ('liked_user',)  

class RetweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retweet
        fields = ('id', 'retweeted_by')
        read_only_fields = ('retweeted_by',) 
                 
                      