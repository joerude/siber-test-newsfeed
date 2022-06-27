from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .settings import dev

urlpatterns = [
                  path('', include('newsfeed.urls')),
                  path('admin/', admin.site.urls),
                  path("ckeditor/", include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if dev.DEBUG:
    import debug_toolbar
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
