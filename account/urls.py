# accounts/urls.py
from django.urls import path
from .views import logout_view, register,  CustomLoginView
#
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]
