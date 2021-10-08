from order.api.views import CartAPIView, ProductCartAPIView,ProductCartsListAPIView,WishlistAPIView,ProductWishlistAPIView,ProductWishlistsAPIView
from django.urls import path
from product.api.views import *

app_name = 'order_api'

urlpatterns =  [ 

    path('cart/<int:pk>',CartAPIView.as_view(),name='cart'),
    path('productcart/<int:pk>',ProductCartAPIView.as_view(),name='productcart '),
    path('productcart/',ProductCartsListAPIView.as_view(),name=' productcarts'),
    path('wishlist/<int:pk>',WishlistAPIView.as_view(),name='cart'),
    path('productwishlist/<int:pk>',ProductWishlistAPIView.as_view(),name='productcart '),
    path('productwishlist/',ProductWishlistsAPIView.as_view(),name=' productcarts'),

]