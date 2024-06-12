from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('message/', message, name='message'),
]