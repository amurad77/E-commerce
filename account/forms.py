from django import forms
from django.contrib.auth import get_user_model,password_validation
from django.core.exceptions import ValidationError
from django.forms import fields, widgets
from django.contrib.auth.forms import ( 
    AuthenticationForm,
    SetPasswordForm,
    UserCreationForm,
    UsernameField,
    PasswordResetForm,
    PasswordChangeForm
)
from django.utils.translation import gettext_lazy as _



User = get_user_model()

class RegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Password'
            }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                'class': 'form-control  ',
                'placeholder': 'Confirm Password'
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta():
        model = User
        fields = (

            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'

        )
        widgets = {

            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control  ',
                'placeholder' : 'First Name',

            }),

            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control  ',
                'placeholder' : 'Last Name',
                
            }),

            'email' : forms.EmailInput(attrs={
                'class' : 'form-control ',
                'placeholder' : 'Email',
                
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control ',
                'placeholder' : 'User Name',
                
            }),
 

        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                                                'class':'form-control ',
                                                'placeholder': 'Username'
                                                }))


    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Password'
            }), 
    )

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Email'
    }), max_length=255)


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Password'
            }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                'class': 'form-control  ',
                'placeholder': 'Confirm Password'
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

class MyPasswordChangeForm(PasswordChangeForm):


    old_password = forms.CharField(

        label=_(" Old Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Write your old password'
            }),
    )
    new_password1 = forms.CharField(
        label=_(" New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Write your new password'
            }),
    )
    new_password2 = forms.CharField(
        label=_(" New Password confirmation"),
        widget=forms.PasswordInput(attrs={
                'class': 'form-control  ',
                'placeholder': '  Confirm your password'
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )