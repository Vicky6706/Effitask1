class IsManagerOrAdminOrReadOnly(BasePermission):
    """
    Read-only for everyone, write access for Manager or Admin.
    """

    def has_permission(self, request, view):
        user = request.user
        if request.method in SAFE_METHODS:
            return True

        if not user.is_authenticated:
            return False

        try:
            role = user.profile.role
        except AttributeError:
            return False

        return role in ['admin', 'manager']

