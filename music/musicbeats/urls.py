from django.urls import path
from . import views

urlpatterns = [
    path('', views.sad, name='sad'),
]
