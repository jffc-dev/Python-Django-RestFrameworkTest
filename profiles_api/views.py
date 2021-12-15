from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, viewsets, filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """ API View de prueba """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del API view"""
        an_apiview = [
            'Usamos métodos HTTP como funciones (get, post, path, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la lógica de nuestra aplicación',
            'Está mapeado manualmente a los URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Maneja actualizar un objeto """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualización parcial de un objeto """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Borrar un objeto """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    def list(self, request):
        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_update',
            'Automáticamente mapea a los URLs usando Routers',
            'Provee más funcionalidad con menos código'
        ]

        return Response({'message': 'Hola', 'a_viewset': a_viewset})

    def create(self, request):
        """ Crear mensaje de hola mundo """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Retornar lista de caracteristicas del API view"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'PUT'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """ Crea tokens de autenticación del usuario """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, )

    def perform_create(self, serializer):
        """ Setear el perfil de usuario de acuerdo al usuario que está logeado"""
        serializer.save(user_profile=self.request.user)
