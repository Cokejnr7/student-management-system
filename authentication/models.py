from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.


class CustomManager(BaseUserManager):
    
    def create_user(self,):
        return 
    
    def create_superuser(self):
        return self.create_user()


# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     username = models.CharField(unique=True)
#     email = models.EmailField(unique=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
    
    
#     USERNAME_FIELDS = username
#     REQUIRED_FIELDS = ['email']