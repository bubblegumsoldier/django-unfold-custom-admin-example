from django.contrib import admin
from django.contrib.auth.models import User
from unfold.admin import ModelAdmin
from unfold.sites import UnfoldAdminSite

from custom_admin.models import CustomGroup, CustomGroupToUser

# Register your models here.
class CustomAdminSite(UnfoldAdminSite):
    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = []
        return custom_urls + urls

custom_admin_site = CustomAdminSite(name="snh2_dj_admin")

@admin.register(User, site=custom_admin_site)
class UserAdmin(ModelAdmin):
    search_fields = ['username', 'email']
    model = User

class CustomGroupToUserInline(admin.TabularInline):
    model = CustomGroupToUser
    autocomplete_fields = ['user', 'group']
    tab = True

@admin.register(CustomGroup, site=custom_admin_site)
class CustomGroupAdmin(ModelAdmin):
    model = CustomGroup
    search_fields = ['name']
    inlines = [CustomGroupToUserInline]
