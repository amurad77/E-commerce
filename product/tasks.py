from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import EmailMessage

from celery import shared_task

from django.template.loader import render_to_string

from django.db.models import Count

from account.models import User

from product.models import Product


@shared_task
def send_mail_to_users():
    
    month = datetime.today() - timedelta(days=30)
    products = Product.objects.filter(created_at__gte=month).annotate(reviews_count = Count('reviews')).order_by('-reviews_count')[:5]
    users = User.objects.filter(last_login__gte=month).values_list('email', flat=True)

    body = render_to_string('email-users.html', context={
        'products': products,
        'users': users,
        'r'
        'SITE_ADDRESS': settings.SITE_ADDRESS
    })
    msg = EmailMessage(subject='Stories News', body=body,
                       from_email=settings.EMAIL_HOST_USER, to=users, )
    msg.content_subtype = 'html'
    msg.send()


# celery -A multi_kart worker --beat --scheduler django --loglevel=info