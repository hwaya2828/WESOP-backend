from django.urls    import path

from products.views import MetaView, ProductListView, DetailProductView

urlpatterns = [
    path('/meta', MetaView.as_view()),
    path('', ProductListView.as_view()),
    path('/<int:product_id>', DetailProductView.as_view())
]