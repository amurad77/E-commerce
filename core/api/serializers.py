from django.db import models
from django.db.models import fields
from django.http import request
from rest_framework import serializers
from core.models import *
from core.api.serializers import *



class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = (
            'email',
        )