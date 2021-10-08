import core
from django.urls import path
from core.api.views import *

app_name = 'subscribe_api'

urlpatterns = [
    path('subscribe/', SubscribeAPIView.as_view(), name = 'subscribe'),
]