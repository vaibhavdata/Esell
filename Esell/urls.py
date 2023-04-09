from django.contrib import admin
from django.urls import path, include
from django.urls import include, re_path as url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/membership/', include('membership.api.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
