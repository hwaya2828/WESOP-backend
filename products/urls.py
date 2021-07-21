from django.urls    import path
from products.views import MetaView, ProductListView, ProductDetailView, PopularProducts

urlpatterns = [
    path('/meta', MetaView.as_view()),
    path('', ProductListView.as_view()),
    path('/product/<int:product_id>', ProductDetailView.as_view()),
    path('/popular', PopularProducts.as_view())
]
