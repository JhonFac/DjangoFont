from django.urls import include, path
from rest_framework.routers import DefaultRouter

from front import views

router = DefaultRouter()

urlpatterns = [
    path("clientes/", views.cliente, name="clientes")
]
