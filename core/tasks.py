# from email.message import EmailMessage
from sys import flags
from celery.app import shared_task
from django.conf import settings
# from django.core.mail.message import EmailMessage
from core.models import *
from product.models import *
import time
from datetime import datetime, timedelta
from account.models import User
from django.template.loader import render_to_string

from django.db.models import Count
from django.core.mail import EmailMessage

@shared_task
def send_mail_to_subscribers():
    
    subscribers = Subscribe.objects.distinct('email').values_list('email',flat = True)
    last_week = datetime.today()-timedelta(days=1)

    product = Product.objects.filter(created_at__gte=last_week).annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:3]
    context = {
        'products': product,
        'SITE_ADDRESS': settings.SITE_ADDRESS,

    }
    body = render_to_string('email-subscribe.html',context )
    subject = 'New product arrived'
    myl = EmailMessage(subject=subject,body=body,
                from_email= settings.EMAIL_HOST_USER,to=subscribers)

# celery -A multi_kart worker --beat --scheduler django --loglevel=info

    myl.content_subtype = 'html'
    myl.send()