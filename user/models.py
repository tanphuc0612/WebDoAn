from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):

    user_id = models.CharField(primary_key=True, default='user_id',unique=True, max_length=16)
    user_name = models.CharField(default='unknown2504', max_length=25)
    email = models.EmailField(default='unknown2504@email.com')
    pass_word = models.CharField(default='unknown2504', max_length=25)

    def __str__(self):
        return f'{self.user_id} Profile'
    

#TODO : hash and salt password