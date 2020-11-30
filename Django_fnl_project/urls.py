from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Django_fnl_project import views as main_views

from Django_fnl_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),
    path('', include('authentication.urls')),
    path('profile/', include('user_profile.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)