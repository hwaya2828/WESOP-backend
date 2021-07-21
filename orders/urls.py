from django.urls  import path
from orders.views import WishListVew, ModifyWishListVew, CartListView, ModifyCartListView, OrderView

urlpatterns = [
    path('/wish', WishListVew.as_view()),
    path('/wish/<int:product_id>', ModifyWishListVew.as_view()),
    path('/cart', CartListView.as_view()),
    path('/cart/<int:product_selection_id>', ModifyCartListView.as_view()),
    path('/order', OrderView.as_view()),
]