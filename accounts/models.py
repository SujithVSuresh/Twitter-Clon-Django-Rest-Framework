from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


class ProfileField(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name='Location')
    people_bio = models.CharField(max_length=247, null=True, blank=True, verbose_name='Bio'), 
    website = models.URLField(null=True, blank=True, verbose_name='Website')
    dob = models.DateField(null=True, blank=True, verbose_name='Date of birth') # Y M D
    joined_on = models.DateField(auto_now_add=True, verbose_name='Joined on')
    profile_photo = models.ImageField(null=True, blank=True, verbose_name='Profile Photo')
    cover_photo = models.ImageField(null=True, blank=True, verbose_name='Cover Photo')  
    biography = models.CharField(max_length=150, null=True, blank=True, verbose_name='Bio')
    follower = models.ManyToManyField(User, related_name='follower', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)


    def __str__(self):
        return str(self.user_name)

class FollowUnfollow(models.Model):
    main_user = models.OneToOneField(ProfileField, on_delete=models.CASCADE, related_name='main_user', verbose_name='Main User', blank=True, null=True)
    follower = models.ManyToManyField(ProfileField, related_name='user_follower', blank=True)
    following = models.ManyToManyField(ProfileField, related_name='user_following', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.main_user)


       
