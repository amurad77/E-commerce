from re import T
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField('First Name', max_length=125)
    email = models.EmailField('Email', max_length=254)
    last_name = models.CharField('Last Name', max_length=125)
    phone_number = CharField(blank=True, help_text='Contact phone number',max_length=15)
    message = models.TextField('Message', max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    


class Subscribe(models.Model):
    email = models.EmailField('Enter you email', max_length=40,unique=True)
    is_active = models.BooleanField(default=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

