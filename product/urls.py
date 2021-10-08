from django.urls import path
from product.views import(
    ProductDetailView,
    ProductListView,
    SearchResultsView,
    )

from product import views

    

app_name = "product"


urlpatterns = [
    path('<int:pk>/',ProductDetailView.as_view(),name="productpage"),
    path('products/',ProductListView.as_view(),name="category"),
    path('search/',SearchResultsView.as_view(),name='search'),
    path('filter-data/',views.filter_data,name='filter_data'),
]
