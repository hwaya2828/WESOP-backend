from django.urls    import path

from products.views import MetaView, DetailProductView

urlpatterns = [
    path('/meta', MetaView.as_view()),
    path('/<int:product_id>', DetailProductView.as_view())
]