import product
from django.urls import path
from product.api.views import *

app_name = 'products_api'

urlpatterns =  [ 

    path('',ProductsAPIView.as_view(),name='products'),
    path('<int:pk>/',ProductAPIView.as_view(),name='product_detail '),
    path('categories/', CategoriesAPIView.as_view(), name = 'categories'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name = 'category_detail'),

]