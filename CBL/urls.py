from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('projects/', include('projects.urls')),
    path('browse/', include('browse.urls')),
    path('dnd/', include('dnd.urls')),
    path('terrarium/', include('terrarium.urls')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
