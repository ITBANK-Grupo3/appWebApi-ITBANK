from rest_framework.routers import DefaultRouter

from database.api.views.clientes_viewsets import ClienteViewSet

router = DefaultRouter()
router.register(r"cliente", ClienteViewSet)

urlpatterns = router.urls
