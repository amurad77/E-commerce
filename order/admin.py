from django.contrib import admin
from order.models import Cart, ProductCart,Wishlist,ProductWishlist


admin.site.register(Cart)
admin.site.register(ProductCart)
admin.site.register(Wishlist)
admin.site.register(ProductWishlist)
