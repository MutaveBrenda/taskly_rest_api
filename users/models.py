import os

from django.db import models
from django.contrib.auth.models import User

from django.utils.deconstruct import deconstructible #allows our class to be converted to a migration

@deconstructible
class GenerateProfileImagePath(object): #create a deconstructable path to where images will be uploaded
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]  #extract extension of our file
        path = f'media/accounts/{instance.user.id}/images/' #define our path
        name = f'profile_image.{ext}' #new name of our file
        return os.path.join(path, name)


user_profile_image_path = GenerateProfileImagePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #define the rship btn users and profile
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'