from django.urls import path
from .views import ProfileView, UserCreateView, FollowView, UnfollowView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:pk>/', UnfollowView.as_view(), name='unfollow'),
    
]
