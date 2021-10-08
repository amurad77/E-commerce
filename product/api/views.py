from product.api.serializers import *
from django.http.response import Http404, JsonResponse
from rest_framework import status
from product.models import *
from product.api.serializers import *
from django.http.response import JsonResponse
from product.api.serializers import *
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductsAPIView(APIView):
    

    def get(self,*args,**kwargs):
        products = Product.objects.all()
        serializer = ProductListSerializer(products,many=True,context = {'request':self.request})
        return JsonResponse (data=serializer.data,safe=False)

    def post(self,*args,**kwargs):
        product_data = self.request.data
        serializer = ProductSerializer (data=product_data, context = {'request':self.request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return JsonResponse (data=serializer.data,safe=False,status = 201)


class ProductAPIView(APIView):

    def get(self,*args,**kwargs):
        product = Product.objects.filter(pk=kwargs.get('pk')).first()
        if not product :
            raise Http404
        serializer = ProductListSerializer(product,context = {'request':self.request})
        return JsonResponse (data=serializer.data,safe=False)

    def delete(self,*args,**kwargs):
        product = Product.objects.filter(pk=kwargs.get('pk'))
        serializer = ProductListSerializer(product,many=True)
        product.delete()
        return JsonResponse(serializer.data,safe=False)

    def put(self, *args, **kwargs):
        product = Product.objects.filter(pk=kwargs.get('pk')).first()
        if not product:
            raise Http404
        serializer = ProductSerializer(data=self.request.data,
                                            instance=product, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False)

class CategoriesAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategoriesSerializer(category, many = True)
        return JsonResponse(data=serializer.data, safe=False)

    def post (self, *args, **kwargs):
        category_data = self.request.data
        serializer = CategoriesCreateSerializer(data=category_data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        category = Category.objects.filter(pk=kwargs.get('pk')).first()
        if not category:
            raise Http404
        serializer = CategoriesSerializer(category)
        return JsonResponse(data=serializer.data, safe=False)


    def delete(self, request,*args,**kwargs):
        category = Category.objects.filter(pk=kwargs.get('pk')).first()
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    def put(self, *args, **kwargs):
        category = Category.objects.filter(pk=kwargs.get('pk')).first()
        if not category:
            raise Http404
        serializer = CategoriesSerializer(data=self.request.data,
                                            instance=category, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)
