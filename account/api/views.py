from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token 
from rest_framework.response import Response
from account.api.serializers import UserDetailSerializer



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = UserDetailSerializer(user)
        return Response(user_serializer.data, status=200)


from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
