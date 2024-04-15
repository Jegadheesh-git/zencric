from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
       return self.email
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(uuid.uuid4())
        super().save(*args, **kwargs)


