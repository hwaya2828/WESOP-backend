from django.contrib import admin
from django.urls    import path, include

urlpatterns = [
    path('user', include('users.urls')),
    path('products', include('products.urls')),
    path('orders', include('orders.urls'))
]
