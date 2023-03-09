from django.urls import path
from .views import UserRegisterView, UserProfile, GetStarted

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/',UserProfile.as_view(), name='profile'),
    path('', GetStarted, name='getstarted')
]