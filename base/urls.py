from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.auth.urls')),
    path('timeline/', include('apps.timeline.urls')),
]
