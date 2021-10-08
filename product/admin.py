from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import (
    Discount, Image, Option, OptionsAttributes, Review,Product,Category,
    ProductAttributes,Brand
)

class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 5

class AttributesProductsInline(admin.TabularInline):
    model = ProductAttributes
    extra = 5

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'title','created_at','updated_at',)
    list_filter = ('rating' ,'created_at','updated_at',)
    search_fields = ('content','rating','title','created_at','updated_at',)

admin.site.register (Review,ReviewAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','created_at','updated_at',)
    list_filter = ( 'price','created_at','updated_at',)
    search_fields = ('price','created_at','updated_at',)
    inlines = (AttributesProductsInline,)
    inlines = (ProductImageInline,)

admin.site.register (Product,ProductAdmin)

class CategoryAdmin(TranslationAdmin):
    list_display = ('title','created_at','updated_at',)
    list_filter = ('title','created_at','updated_at',)
    search_fields = ('title','created_at','updated_at',)

admin.site.register (Category,CategoryAdmin)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('types','is_active','amount', 'created_at','updated_at',)
    list_filter = ('types','is_active','amount', 'created_at','updated_at',)
    search_fields = ('types','is_active','amount', 'created_at','updated_at',)

admin.site.register (Discount,DiscountAdmin)


class OptionAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at',)
    list_filter = ('title','created_at','updated_at',)
    search_fields = ('title','created_at','updated_at',)

admin.site.register (Option,OptionAdmin)


class OptionAttributesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

admin.site.register (OptionsAttributes,OptionAttributesAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

admin.site.register (Brand,BrandAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('created_at','product')
    list_filter = ('created_at','product')
    search_fields = ('img','created_at',)

admin.site.register (Image,ImageAdmin)

admin.site.register(ProductAttributes)  

