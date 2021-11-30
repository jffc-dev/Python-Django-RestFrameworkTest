from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serializa un campo de prueba """
    name = serializers.CharField(max_length=10)