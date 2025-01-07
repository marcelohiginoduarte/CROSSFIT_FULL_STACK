from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TreinoViewSet

router = DefaultRouter()
router.register(r'treinos', TreinoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
