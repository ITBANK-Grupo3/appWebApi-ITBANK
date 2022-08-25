from django.urls import path, include
from rest_framework.routers import DefaultRouter

from database.api.views import (
    clientes_viewsets,
    cuentas_viewsets,
    prestamos_viewsets,
    tarjetas_viewsets,
)

router = DefaultRouter()
router.register(r"clientes", clientes_viewsets.ClienteViewSet)
router.register(r"cuentas", cuentas_viewsets.CuentaViewSet)
router.register(r"prestamos", prestamos_viewsets.PrestamosViewSet)
router.register(r"tarjetas", tarjetas_viewsets.TarjetaViewSet)
router.register(r"sucursales", prestamos_viewsets.SucursalViewSet)


urlpatterns = router.urls
