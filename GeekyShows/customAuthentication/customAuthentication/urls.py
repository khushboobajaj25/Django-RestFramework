from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',obtain_auth_token),
]