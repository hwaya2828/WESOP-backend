from django.urls    import path
from users.views    import UserInformationView



urlpatterns = [
            path('/information', UserInformationView.as_view()),
]