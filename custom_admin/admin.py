from django.contrib import admin
from django.contrib.auth.models import User
from unfold import admin as unfold_admin


# Register your models here.
class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = []
        return custom_urls + urls


class UserAdmin(unfold_admin.ModelAdmin):
    model = User


custom_admin_site = CustomAdminSite(name="snh2_dj_admin")
custom_admin_site.register(User, UserAdmin)