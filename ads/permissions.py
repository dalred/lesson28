from rest_framework import permissions

from users.models import User


class SelectionUpdateDeletePermission(permissions.BasePermission):
    message = "Sorry you can't do this, Updating or Delete not your Selection is not permitted"

    # Obj - объект queryset
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.owner.id:
            return True
        elif request.user.role in ([User.admin, User.moderator]):
            return True
        return False


class SelectionCheckRolePermission(permissions.BasePermission):
    message = "Sorry you can't do this, you are not moderator or admin"

    def has_permission(self, request, view):
        if request.user.role not in ([User.admin, User.moderator]):
            return False
        return True


class CommentsUpdateDeletePermission(permissions.BasePermission):
    message = "Sorry you can't do this, Updating or Delete not your comment is not permitted"

    # Obj - объект queryset(get by number/update/)
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.author.id:
            return True
        elif request.user.role in ([User.admin, User.moderator]):
            return True
        return False