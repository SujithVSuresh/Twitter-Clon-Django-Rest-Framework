from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import ProfileField, FollowFollowing
from .serializers import ProfileSerializer, RegisterUserSerializer, FollowingSerializer

# Create your views here.
class ProfileView(generics.RetrieveUpdateAPIView): 
    queryset = ProfileField.objects.all() 
    serializer_class = ProfileSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer

class FollowingView(generics.ListCreateAPIView):
    serializer_class = FollowingSerializer

    def get_queryset(self):
        self.name = get_object_or_404(ProfileField, id=self.kwargs['pk'])
        return FollowFollowing.objects.filter(followers=self.name)

    def perform_create(self, serializer):
        self.following = get_object_or_404(ProfileField, id=self.kwargs['pk'])
        self.followers = ProfileField.objects.get(user_name=self.request.user)
        serializer.save(following=self.following, followers=self.followers) 

class FollowerView(generics.ListAPIView):
    serializer_class = FollowingSerializer  

    def get_queryset(self):
        self.name = get_object_or_404(ProfileField, id=self.kwargs['pk'])  
        return FollowFollowing.objects.filter(following=self.name) 

   

 