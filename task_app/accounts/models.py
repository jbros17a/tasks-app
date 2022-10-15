from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 

from .managers import CustomUserManager

class UserAccount(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(_("email address"), max_length=60, unique=True)
    username = models.CharField(_("username"), max_length=30, unique=True)
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), auto_now=True)

    is_staff = models.BooleanField(_("user is staff"), default=False)
    is_active = models.BooleanField(_("user is active"), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + self.last_name