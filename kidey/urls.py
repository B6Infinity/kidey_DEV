from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sudo/', include('admin.urls')),
]
