
from rest_framework.permissions import IsAuthenticated
from .models import Estudiante
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProjecViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializers
    queryset = Estudiante.objects.all()
