from core.views import AboutPageView, FaqView, NotFoundView, ProductListView
from django.urls import path

from core.views import CreateContactView
app_name = "core"

urlpatterns = [
    path('contact/',CreateContactView.as_view(),name='contact'),
    path('',ProductListView.as_view(),name="index"),
    path('404/',NotFoundView.as_view(),name='404'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('faq/',FaqView.as_view(),name="faq"),
    
    
]
