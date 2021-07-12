from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class AccountManager(BaseUserManager):

    #This is a manager for Account Class
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Email address")

        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user