from rest_framework.permissions import BasePermission
class Uprawnienia(BasePermission):
    def has_permission(self, request, view):
        wymagane_uprawnienia = ['aplikacja.view_uzytkownik']
        return all(request.user.has_perm(permission) for permission in wymagane_uprawnienia)
