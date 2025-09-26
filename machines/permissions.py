from rest_framework import permissions

class ReadOnlyOrAdmin(permissions.BasePermission):
    """
    Permite GET/HEAD/OPTIONS a cualquiera,
    pero requiere admin para POST/PUT/PATCH/DELETE.
    """
    def has_permission(self, request, view):
        # Métodos "seguros" => GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Solo admins para métodos de escritura
        return request.user and request.user.is_staff
