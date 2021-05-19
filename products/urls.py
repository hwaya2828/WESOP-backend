from django.urls    import path

from products.views import PopularProduct

urlpatterns = [
    path('/popular', PopularProduct.as_view())
]