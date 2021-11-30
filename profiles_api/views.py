from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ API View de prueba """

    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del API view"""
        an_apiview = [
            'Usamos métodos HTTP como funciones (get, post, path, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la lógica de nuestra aplicación',
            'Está mapeado manualmente a los URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
