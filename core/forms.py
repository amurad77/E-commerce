from django.forms import ModelForm
from django.db.models import fields
from core.models import Contact
from django import forms




class ContactForm(forms.ModelForm):
    

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email', 
            'message',
            'phone_number' 
        )

        widgets = {
            'first_name' : forms.TextInput(attrs={
                                'class': 'form-control ',
                                'placeholder' : 'Enter your Name...'
            }),
            'last_name' : forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Enter your Last Name...'
            }),
            'phone_number' : forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Enter your Number...'
            }),
            'email' : forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Enter your Email....'
            }),
            'message' : forms.Textarea(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Enter your Message....'
            }),
         
        }