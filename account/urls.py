from django.urls import path
from account.views import (
    CustomPasswordResetConfirmView,
    CustomLoginView,
    ProfileView,
    VendorView,
    logout,
    RegisterView,
    activate,
    CustomPasswordResetView,
    MyPasswordChangeView
)


app_name = "account"

urlpatterns = [
    path('forget/',CustomPasswordResetView.as_view(),name="forget"),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('activate/<str:uidb64>/<str:token>',activate,name='confirmation'),
    path('reset_password/<str:uidb64>/<str:token>/',CustomPasswordResetConfirmView.as_view(),name='reset-password'),
    path('changepassword/',MyPasswordChangeView.as_view(),name='change_password'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('register/',RegisterView.as_view(),name='register'),
    path('vendor/',VendorView.as_view(),name="vendor"),]