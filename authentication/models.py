from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomManager(BaseUserManager):
    
    def create_user(self,username,email,password,**other_fields):
        if not username:
            raise ValueError(_('You must provide a username.'))
        
        if not email:
            raise ValueError(_('You must provide an email address.'))
        
        email = self.normalize_email(email)
        
        user = self.model(username=username,email=email,**other_fields)
        
        user.set_password(password)
        
        user.save()
        
        return user
    
    
    
    def create_superuser(self,username,email,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be assigned is_superuser=True'))

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned is_staff=True'))

        return self.create_user(username,email, password, **other_fields)
    
    


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(unique=True,max_length=50)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects= CustomManager()
    
    def __str__(self):
        return self.username