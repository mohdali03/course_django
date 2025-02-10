from django.urls import path
from .views import create, delete, show, update

urlpatterns = [
    path('course/', create, name="create"),
    path('delete/', delete, name="delete"),
    path('update/', update, name='update'),
    path('', show, name='home'),
]