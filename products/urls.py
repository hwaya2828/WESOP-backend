from django.urls    import path

from products.views import DetailProductView

urlpatterns = [
    path('/product/<int:product_id>', DetailProductView.as_view())
]