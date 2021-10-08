from product.models import Review
from django.forms import ModelForm
from django.db.models import fields
from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="New Item")


class ReviewForm(ModelForm):


    class Meta:
        model = Review
        fields = (
            'name',
            'email',
            'title',
            'content',
            'rating',

        )
        widgets = {

            'name' : forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Enter your Name'
            }),
            'email' : forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Enter your Email'
            }),
            'title' : forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Enter your Review subjects ...'
            }),
            'content' : forms.TextInput(attrs={
                                'class': 'form-control ',
                                'placeholder' : 'Write Your Testimonial here...'
            })
            
        }