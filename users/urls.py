from django.urls    import path
from users.views    import UserInformationView, SignupView, LoginView

urlpatterns = [
            path('/information', UserInformationView.as_view()),
            path('/signup', SignupView.as_view()),
            path('/login', LoginView.as_view())
]