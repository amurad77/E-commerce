
from django.urls import path
from account.api.views import RegisterView

app_name = 'account_api'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api_register'),
    
]