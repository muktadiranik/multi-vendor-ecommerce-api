from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from . models import *

from apps.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email", "user_image", "user_cover",
         "street", "city", "state", "zip_code", "area_code", "phone_number", "country")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser", 'street', 'city', 'state', 'zip_code', 'area_code']
    search_fields = ["name"]


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']


@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    list_display = ['user', 'document']


class SiteAdmin(SiteAdmin):
    list_display = ('name', 'domain')

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)
