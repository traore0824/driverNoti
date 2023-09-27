from rest_framework.permissions import BasePermission

class MyPermision(BasePermission):
    def has_permission(self, request, view):
        if request.method == "PUT":
            if request.user.groups.filter(name= "Chauffeur").exists():
                return True 
        elif request.method in ["GET", "POST", "DELETE", "PATCH"]:
            return True