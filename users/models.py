from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, primary_key = True, verbose_name='아이디')
    password = models.CharField(max_length=30, verbose_name = '비밀번호')
    email = models.CharField(max_length=40, verbose_name = '이메일')
    business_number = models.CharField(max_length=10, blank = True, verbose_name = '사업자번호')
    profile_image = models.ImageField(upload_to="users/profile", blank = True, verbose_name='프로필사진')

# class User(models.Model):
#    pass