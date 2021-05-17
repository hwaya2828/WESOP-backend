from django.urls    import path
from orders.views    import CartAddView, CartDeleteView, CartQuantityView, CartCheckView



urlpatterns = [
            path('/Cartadd', CartAddView.as_view()),
            path('/Cartdelete', CartDeleteView.as_view()),
            path('/Cartquantity', CartQuantityView.as_view()),
            path('/Cartcheck', CartCheckView.as_view())
]