from django.urls import path
from order.views import CheckoutView,CartView, OrderSuccessView,WishlistView

app_name = "order"

urlpatterns = [
    
        path('checkout/',CheckoutView.as_view(),name="checkout"),
        path('cart/',CartView.as_view(),name="cart"),
        path('wishlist/',WishlistView.as_view(),name="wishlist"),
        path('ordersuccess/',OrderSuccessView.as_view(),name="ordersuccess"),
  
    ]

