from django.urls import path
from custom_admin.admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
]
