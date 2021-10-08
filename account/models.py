import django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True,)
    GENDER_CHOICES = (
        (True, 'Men'),
        (False, 'Woman'),
    )
    image = models.ImageField('Image', upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)
    gender = models.BooleanField('Gender', choices=GENDER_CHOICES, default=False)