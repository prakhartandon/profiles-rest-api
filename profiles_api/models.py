from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    def create_user(self, email, user, password=None):
         if not email:
             raise ValueError('User must have an email address')
         email = self.normalize_email(email)
         user = self.model(email=email, name=name)

         user.setpassword(password)
         user.save(using=self._db)

         return User

    def create_superuser(self, email, user, password):
        """Create and save a new superuser with given details"""
        user=self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Databse Model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELS=['name']

    def get_full_name(self):
        """ Retrive Full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of User"""
        return self.name

    def __str__(self):
        """Return String respresentation of user"""
        return self.email

# Create your models here.
