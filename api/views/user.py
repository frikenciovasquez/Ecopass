from rest_framework import status, viewsets
#from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
    IsAuthenticated,
)
# Serializers
from ..serializers import UserLoginSerializer, UserSerializer , UserSingUpSerializer
# Models
from ..models import User

class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
 
    @permission_classes([AllowAny])
    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSingUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = Token.objects.get_or_create(user=user)[0].key
        data = {"user": UserSerializer(user).data, "access_token": token}

        return Response(data, status=status.HTTP_201_CREATED)

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["get"])
    def logout(self, request):
        request.user.auth_token.delete()
        return Response(
            {"Éxito": "Sesión cerrada correctamente"}, status=status.HTTP_200_OK
        )