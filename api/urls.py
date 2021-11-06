from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,TravelViewSet,RuteViewSet,ServicioViewSet
    
)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="usuarios")
router.register(r"travel",TravelViewSet,basename="Viajes")
router.register(r"ruta",RuteViewSet,basename="Ruta")
router.register(r"servicio",ServicioViewSet,basename="servicio")
urlpatterns = [
    path("", include(router.urls)),
]