from rest_framework import response, status
from order.models import Cart, ProductCart,Wishlist,ProductWishlist
from order.api.serializers import CartSerializer, ProductCartSerializer,WishlistSerializer,ProductWishlistSerializer,ProductCartListSerializer,ProductWishlistsSerializer
from product.models import *
from product.api.serializers import *
from product.api.serializers import *
from rest_framework.generics import *

class CartAPIView(RetrieveAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    


class ProductCartAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCartSerializer


    def get_queryset(self):
        return ProductCart.objects.filter(cart=self.request.user.cart)


class ProductCartsListAPIView(ListCreateAPIView):
    serializer_class = ProductCartSerializer


    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.serializer_class = ProductCartListSerializer
        elif request.method == 'POST':
            self.serializer_class = ProductCartSerializer
        return super().dispatch(request, *args, **kwargs)
    

    def get_queryset(self):
        return ProductCart.objects.filter(cart=self.request.user.cart)


class WishlistAPIView(RetrieveAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
    


class ProductWishlistAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductWishlistSerializer


    
   

    def get_queryset(self):
        return ProductWishlist.objects.filter(wishlist=self.request.user.wishlist)


class ProductWishlistsAPIView(ListCreateAPIView):
    serializer_class = ProductWishlistSerializer


    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.serializer_class = ProductWishlistsSerializer
        elif request.method == 'POST':
            self.serializer_class = ProductWishlistSerializer
        return super().dispatch(request, *args, **kwargs)
    


    def get_queryset(self):
        return ProductWishlist.objects.filter(wishlist=self.request.user.wishlist)



   


   
