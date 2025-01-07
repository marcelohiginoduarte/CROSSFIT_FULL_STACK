from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanoTreinoViewSet

router = DefaultRouter()
router.register(r'planos', PlanoTreinoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]