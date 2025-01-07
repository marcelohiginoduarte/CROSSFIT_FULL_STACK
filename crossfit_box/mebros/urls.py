from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembroViewSet


router = DefaultRouter()
router.register(r'membros', MembroViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]