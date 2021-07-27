from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from .managers import AccountManager
# Custom user created.
class Account(AbstractBaseUser):
    #Custom user class inheriting AbstractBaseUser class
    username   = models.CharField(max_length=255, unique=True)
    email      = models.EmailField(unique=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date join', auto_now_add=True)
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        #Simplest possible answer: Yes, always
        return True
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("profile:profile_view", kwargs={"pk": self.pk})
