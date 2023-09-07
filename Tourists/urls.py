from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from report import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewset)
router.register(r'coords', views.CoordsViewset)
router.register(r'mount', views.MountViewset)
router.register(r'photo', views.PhotoViewset)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
