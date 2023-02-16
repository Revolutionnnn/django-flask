from rest_framework import routers
from .api import ProjecViewSet

routers = routers.DefaultRouter()

routers.register('api/estudiantes', ProjecViewSet, 'estudiantes')

urlpatterns = routers.urls
