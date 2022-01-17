from rest_framework import serializers
from .models import ProfileField, FollowFollowing
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    class Meta:
        model = ProfileField
        fields = ('id', 'profile_photo', 'cover_photo', 'user_name', 'name', 'following', 'followers', 'biography', 'location', 'website', 'dob', 'joined_on')
        read_only_fields = ('user_name', 'joined_on', 'following', 'followers')

    def get_following(self, pk):
        return FollowFollowing.objects.filter(followers=pk).count() 

    def get_followers(self, pk):
        return FollowFollowing.objects.filter(following=pk).count()         

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowFollowing
        fields = ('id', 'following', 'followers', 'created')
        read_only_fields = ('created', 'following', 'followers')        

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()    
        return instance 