from django.urls import path
from . import views

urlpatterns = [
    path('', views.sellers_list)
]
