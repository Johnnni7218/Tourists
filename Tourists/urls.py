from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mount', MountViewSet, basename='mount')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submitData/', include(router.urls))
]
