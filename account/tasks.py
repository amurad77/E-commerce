from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string 
from django.conf import settings
from django.urls.base import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from account.utils.token import account_activation_token




def send_confirmation_mail(user):

    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    redirect_url = f"http://localhost:8000{reverse_lazy('account:confirmation', kwargs={'uidb64': uid,'token': token})}"
    body = render_to_string('email/confirmation_email.html', context={
        
        'user': user,
        'redirect_url' : redirect_url

    })

    myl = EmailMessage(subject="Email Verification",body=body,
                from_email= settings.EMAIL_HOST_USER,to=[user.email])

    myl.content_subtype = 'html'
    myl.send()
