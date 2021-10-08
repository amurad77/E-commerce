
from django.views.generic import TemplateView

class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class WishlistView(TemplateView):
    template_name = 'wishlist.html'


class OrderSuccessView(TemplateView):
    template_name = 'order-success.html'
