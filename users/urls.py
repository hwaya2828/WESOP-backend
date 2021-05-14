from django.urls    import path
from users.views import SignupView, LoginView, SkintypeView, AddressView



urlpatterns = [
            path('/signup', SignupView.as_view()),
            path('/login', LoginView.as_view()),
            path('/skin', SkintypeView.as_view()),
            path('/address', AddressView.as_view())
]