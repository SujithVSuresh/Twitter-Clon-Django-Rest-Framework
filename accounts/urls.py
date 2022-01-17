from django.urls import path
from .views import ProfileView, UserCreateView, FollowingView, FollowerView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('following/<int:pk>/', FollowingView.as_view(), name='following'),
    path('follower/<int:pk>/', FollowerView.as_view(), name='follower'),
]
