from django.db import models
from django.db.models import fields
from django.http import request
from rest_framework import serializers
from product.models import *
from product.api.serializers import *

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'parent_cat',
        )

class CategoriesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'parent_cat',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created_at',
            'updated_at',
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta :
        model = Brand 
        fields = [
            'id',
            'title',

        ]

class OptionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Option
        fields = (
            'id',
            'title',
        )

class OptionsAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsAttributes
        fields = (
            'id',
            'title',

        )


class ProductAtributesSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductAttributes 
        fields = [
            'id'
            'optionattributes',
            'stock',
            'created_at',
            'updated_at'

        ]




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (       
            'title',
            'price',
            'shortdetail' ,
            'image' ,
            'longdetail' ,
            'video' ,
            'created_at',
            'updated_at',
            'brand',
            'category',
            'productattribute',
            'get_sale_price',
            'get_absolute_url'
        )
      



class ProductListSerializer(ProductSerializer):
    productattribute = OptionsAttributesSerializer(many=True)
    category = CategorySerializer()
    brand = BrandSerializer()
