from django.urls import path
from .views import register_request, login_request

urlpatterns = [
    path("signup/", register_request, name="signup"),
    path("signin/", login_request, name="signin"),

]
