from django.urls    import path
from users.views    import SkintypeView, AddressView, SkintypedeleteView, AddressdeleteView



urlpatterns = [
            path('/skin', SkintypeView.as_view()),
            path('/address', AddressView.as_view()),
            path('/skindelete', SkintypedeleteView.as_view()),
            path('/addressdelete', AddressdeleteView.as_view())
]