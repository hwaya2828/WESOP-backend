from django.urls import path

from products.views import MetaView

urlpatterns = [
    path('/meta', MetaView.as_view())
]