from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register, login, me, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path("register/", register),
    path("login/", login),
    path("me/", me),

    path("profile/", ProfileDetailView.as_view()),
    path("profile/update/", ProfileUpdateView.as_view()),

    path("token/refresh/", TokenRefreshView.as_view()),
]
