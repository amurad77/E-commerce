from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from account.api.views import CustomAuthToken




urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/',include('product.api.urls' ,namespace = 'products_api')),
    path('api/order/',include('order.api.urls' ,namespace = 'order_api')),
    path('api/',include('core.api.urls' ,namespace = 'subscribe_api')),

    path('social-auth/', include('social_django.urls', namespace="social")),
    path('api-token-auth/',CustomAuthToken.as_view()),
    path('api/product/', include('product.api.urls', namespace='category_api')),
    path('api/account/', include('account.api.urls', namespace='account_api')),
    path('api-auth/', include('rest_framework.urls'))


]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    
    path("",include("core.urls",namespace="core")),
    path("account/",include("account.urls",namespace="account")),
    path("order/",include("order.urls",namespace="order")),
    path("product/",include("product.urls",namespace="product")),
)
