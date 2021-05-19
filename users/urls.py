from django.urls    import path
from users.views    import UserInformationView



urlpatterns = [
            path('/userinformation', UserInformationView.as_view()),
]