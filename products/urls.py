from itertools import product
from django.urls    import path

from products.views import MetaView, DetailProductView, PopularProduct

urlpatterns = [
    path('/meta', MetaView.as_view()),
    path('/<int:product_id>', DetailProductView.as_view()),
    path('/popular', PopularProduct.as_view())
]