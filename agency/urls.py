from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', include('pages.urls')),
    path('trips/', include('trips.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
