from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('api-auth/', include('django.contrib.auth.urls')),  # Use 'path' here
    #re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),  # Use 're_path' for regular expressions
]
