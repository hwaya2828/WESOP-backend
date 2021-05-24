from django.urls  import path
from orders.views import CartView, OrderCheckView, OrderGetView

urlpatterns = [
            path('/cart', CartView.as_view()),
            path('/cart/<int:cart_id>', CartView.as_view()),
            path('/order', OrderCheckView.as_view()),
            path('/log', OrderGetView.as_view())
]