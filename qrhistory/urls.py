from django.urls import path
from .views import save_qr, history, delete_qr, register
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("register/", register),
    path("login/", TokenObtainPairView.as_view()),
    path("save/", save_qr),
    path("history/", history),
    path("delete/<int:pk>/", delete_qr)
]