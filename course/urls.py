from django.urls import path
from .views import create, delete, show, update
urlpatterns = [
    path('course/', create),
    path('delete/', delete),
    path('update/', update ),
    path('home/', show),
]