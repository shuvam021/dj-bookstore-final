from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    # auth
    path("register/", views.RegistrationAPIView.as_view(), name="register"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("verify/<str:token>", views.verify_user_view, name="verify_user"),
    # inventory
    path("book/", views.BookAPIView.as_view(), name="book-list"),
    path("book/<int:pk>/", views.BookAPIView.as_view(), name="book-detail"),
]
