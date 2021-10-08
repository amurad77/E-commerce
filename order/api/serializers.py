from order.models import Cart,ProductCart,Wishlist,ProductWishlist
from rest_framework import serializers
from product.models import *
from product.api.serializers import ProductListSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'products',
        )
    



class ProductCartSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductCart 
        fields = [
            'id',
            'cart',
            'product',
            'quantity',

        ]
        read_only_fields = ('cart',)


    def validate(self, attrs):
        request = self.context.get('request')
        attrs['cart'] = request.user.cart
        return super().validate(attrs)


class ProductCartListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    class Meta :
        model = ProductCart 
        fields = [
            'id',
            'cart',
            'product',
            'quantity',

        ]
        read_only_fields = ('cart',)


    def validate(self, attrs):
        request = self.context.get('request')
        attrs['cart'] = request.user.cart
        return super().validate(attrs)


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'user',
        )
    

class ProductWishlistSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductWishlist 
        fields = [
            'id',
            'wishlist',
            'product',

        ]
        read_only_fields = ('wishlist',)

    def validate(self, attrs):
        request = self.context.get('request')
        attrs['wishlist'] = request.user.wishlist
        return super().validate(attrs)


class ProductWishlistsSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    class Meta :
        model = ProductWishlist
        fields = [
            'id',
            'wishlist',
            'product',

        ]
        read_only_fields = ('wishlist',)








