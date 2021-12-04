from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Permite al usuario editar su propio perfil """

    def has_object_permission(self, request, view, obj):
        """ Verificar si el usuario está intentando editar su prio perfil """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
