import math
from math import *
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import  CharField
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    title = models.CharField('Title', max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    parent_cat = models.ForeignKey("self",on_delete=models.CASCADE,db_index=True,related_name="parent",null=True,blank=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
       
    def __str__(self):
        return self.title


class Discount(models.Model):
    Type_of_discount = [
        (1, '%'),
        (2, 'vahid'),
        
    ]
    title = models.CharField(max_length=100,null=True,blank=True)
    types = models.IntegerField(choices=Type_of_discount)
    is_active = models.BooleanField(default=True)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.title

 
class Option(models.Model):
    title = CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE,db_index=True,related_name="options")



    def __str__(self):
        return self.title

class OptionsAttributes(models.Model):
    title = CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    option = models.ForeignKey(Option,on_delete=CASCADE,db_index=True,related_name="attributes")

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    shortdetail = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/products')
    longdetail = models.TextField()
    video = models.CharField(max_length=500,null=True,blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,db_index=True,related_name='products',null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,db_index=True,related_name="products")
    discount = models.ForeignKey(Discount,on_delete=models.SET_NULL,db_index=True,related_name="products",null=True,blank=True)
    productattribute = models.ManyToManyField(OptionsAttributes,through="ProductAttributes",related_name="attributes")

    def __str__(self):
        return self.title

    def get_discount(self):
        if self.discount and self.discount.is_active:
            return True
        else:
            return False
    
    def get_sale_price(self):
        if self.get_discount() == True:
            if self.discount.types == 1 :
                return self.price - (self.price / 100 * self.discount.amount)
            else :
                return self.price - self.discount.amount
        return self.price

    def get_sale_percent(self):
        if self.get_discount() == True:
            if self.discount.types == 1 : 
                return self.discount.amount
            else:
                percentofprice = (self.discount.amount * 100) / self.price
                return math.floor(percentofprice)

    def avarage_rating(self):
        rating_list = list(self.reviews.values_list('rating', flat=True))
        avarageofrating = sum(rating_list)/len(rating_list)
        return avarageofrating

    def get_absolute_url(self):
        return reverse_lazy("product:productpage", kwargs={"pk": self.pk})


    


class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="attributess")
    optionsattribute = models.ForeignKey(OptionsAttributes, on_delete=models.CASCADE)
    stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title


class Image(models.Model):
    img = models.ImageField(upload_to = 'products')
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=CASCADE,db_index=True,related_name='images')


class Review(models.Model):
    Rating_of_products = [
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
        
    ]

    name = models.CharField('Name', max_length=125)
    email = models.CharField('Email', max_length=125)
    title =  models.CharField('Title', max_length=125)
    content = models.CharField('Content', max_length=500)
    rating = models.IntegerField("Rating",choices=Rating_of_products)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)


    product = models.ForeignKey(Product,on_delete=models.CASCADE,db_index=True,related_name="reviews")
    
