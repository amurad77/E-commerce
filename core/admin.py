from django.contrib import admin
from core.models import Contact, Subscribe

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'email' ,"message",'created_at',)
    list_filter = ( "email" ,"message",'created_at',)
    search_fields = ( "email" ,"message",'created_at',)

admin.site.register (Contact,ContactAdmin)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email','is_active','create_at','update_at',)
    list_filter = ('email','is_active','create_at','update_at',)
    search_fields = ('email','is_active','create_at','update_at',)

admin.site.register(Subscribe)








