class ViewPermissionsMixin:
    def has_add_permissions(self):
        return False

    def has_remove_permissions(self, obj):
        return False

    def has_update_permissions(self, obj):
        return False

    def has_view_permissions(self, obj):
        return True
