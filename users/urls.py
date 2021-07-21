from django.urls import path
from users.views import SignUpView, SignInView, UserInformationView, ModifyUserInformationView

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/user', UserInformationView.as_view()),
    path('/user/<int:user_id>', ModifyUserInformationView.as_view()),
]