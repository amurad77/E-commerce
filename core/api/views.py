from product.api.serializers import *
from core.models import *
from core.api.serializers import *
from rest_framework.generics import CreateAPIView


class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscribeSerializer
    model = Subscribe

   