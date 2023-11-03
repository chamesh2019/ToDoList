from .views import home, reset
from django.urls import path

urlpatterns = [
    path('home/', home, name='home'),
    path('reset/', reset, name='reset'),
]