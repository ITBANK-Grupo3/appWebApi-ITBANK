from rest_framework.routers import DefaultRouter

from database.api.views.clientes_viewsets import ClienteViewSet, CuentaViewSet

router = DefaultRouter()
router.register(r"cliente", ClienteViewSet)
router.register(r"cuenta", CuentaViewSet)

urlpatterns = router.urls
