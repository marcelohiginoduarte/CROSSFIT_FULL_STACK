from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mebros', include('mebros.urls')),
    path('planotreino', include('planotreino.urls')),
    path('treino', include('treino.urls')),
]
