from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.my_list),
    path("potato/", views.hello2),
]
