from django.urls import path
from .views import TweetView, TweetDetailView, CommentView, LikeView, RetweetView

urlpatterns = [
    path('', TweetView.as_view(), name='tweet'),
    path('tweet/<str:pk>/', TweetDetailView.as_view(), name='tweet-detail'),
    path('tweet/<str:pk>/retweet/', RetweetView.as_view(), name='retweet'),
    path('tweet/<str:pk>/like/', LikeView.as_view(), name='like'),
    path('comment/<str:pk>/', CommentView.as_view(), name='comment'),
]
