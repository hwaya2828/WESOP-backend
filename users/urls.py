from django.urls    import path
from users.views    import UserInformationView



urlpatterns = [
            path('/userinfo', UserInformationView.as_view()),
]