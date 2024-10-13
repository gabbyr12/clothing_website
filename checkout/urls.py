from django.urls import path
from .views import index, fly

urlpatterns = [
    path('', index, name='index'),
    path('fly', fly, name='fly'),
]
