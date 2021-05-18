from django.urls    import path
from orders.views    import CartView, OrderCheckView



urlpatterns = [
            path('/cart', CartView.as_view()),
            path('/ordercheck', OrderCheckView.as_view())
]