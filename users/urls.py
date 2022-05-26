from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('sign-up/', SignUpView, name="sign-up"),
]