from django.db.models.fields.related import OneToOneField
import order
from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class Cart(models.Model):
    user = OneToOneField(User,related_name='cart',on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,through="ProductCart",related_name="cart")

    class Meta:
        verbose_name = 'Cart'

    def total_price(self):
        sum = 0
        cartproducts = self.cartproducts.all()
        for cartproduct in cartproducts:
            sumofproducts  = cartproduct.product.get_sale_price() * cartproduct.quantity
            sum += sumofproducts 
        return sum

        


class ProductCart(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="cartproducts")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cartproducts')
    quantity = models.PositiveIntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.product.title

    
    def cartofprice(self):
        return self.product.get_sale_price() * self.quantity


class Wishlist(models.Model):
    user = OneToOneField(User,related_name='wishlist',on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,through="ProductWishlist",related_name="wishlist")

    class Meta:
        verbose_name = 'Wishlist'



class ProductWishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="wishlistproducts")
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE,related_name='wishlistproducts')

    def __str__(self):
        return self.product.title

