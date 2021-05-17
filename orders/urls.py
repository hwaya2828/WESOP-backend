from django.urls    import path
from orders.views    import CartAddView, CartDeleteView, CartQuantityView, CartCheckView, OrderCheckView



urlpatterns = [
            path('/cartadd', CartAddView.as_view()),
            path('/cartdelete', CartDeleteView.as_view()),
            path('/cartquantity', CartQuantityView.as_view()),
            path('/cartcheck', CartCheckView.as_view()),
            path('/ordercheck', OrderCheckView.as_view())
]