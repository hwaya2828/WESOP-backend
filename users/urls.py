from django.urls    import path
from users.views    import UserInformationView, SignUpView, LoginView

urlpatterns = [
            path('/information', UserInformationView.as_view()),
            path('/signup', SignUpView.as_view()),
            path('/login', LoginView.as_view())
]