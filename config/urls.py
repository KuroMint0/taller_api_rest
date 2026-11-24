from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from eventos.api import EventoViewSet

router = DefaultRouter()
router.register("eventos", EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

