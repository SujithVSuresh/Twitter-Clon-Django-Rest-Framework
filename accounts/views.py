from django.shortcuts import render, get_object_or_404
from django.http import Http404, request
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import ProfileField, FollowUnfollow
from .serializers import ProfileSerializer, RegisterUserSerializer, FollowUnfollowSerializer

# Create your views here.
class ProfileView(generics.RetrieveUpdateAPIView): 
    queryset = ProfileField.objects.all() 
    serializer_class = ProfileSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer

class FollowView(APIView):
    def get_object(self, pk):
        try:
            return FollowUnfollow.objects.get(main_user=pk)
        except FollowUnfollow.DoesNotExist:
            raise Http404

    def get_profile(self, pk):
        try:
            return ProfileField.objects.get(id=pk)
        except ProfileField.DoesNotExist:
            raise Http404        

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = FollowUnfollowSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        profile = self.get_profile(pk)
        serializer = FollowUnfollowSerializer(user, data=request.data)
        if serializer.is_valid():
            #follower
            req_user = ProfileField.objects.get(user_name=request.user)
            user.follower.add(req_user)
            #following
            followinguser = self.get_object(req_user.pk)
            followinguser.following.add(profile)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnfollowView(APIView):
    def get_object(self, pk):
        try:
            return FollowUnfollow.objects.get(main_user=pk)
        except FollowUnfollow.DoesNotExist:
            raise Http404

    def get_profile(self, pk):
        try:
            return ProfileField.objects.get(id=pk)
        except ProfileField.DoesNotExist:
            raise Http404        

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = FollowUnfollowSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        profile = self.get_profile(pk)
        serializer = FollowUnfollowSerializer(user, data=request.data)
        if serializer.is_valid():
            #follower
            req_user = ProfileField.objects.get(user_name=request.user)
            user.follower.remove(req_user)
            #following
            followinguser = self.get_object(req_user.pk)
            followinguser.following.remove(profile)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

 