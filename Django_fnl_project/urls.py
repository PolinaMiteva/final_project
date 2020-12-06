from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Django_fnl_project import views as main_views
from Django_fnl_project import settings

urlpatterns = [
    path('', main_views.index, name='index'),
    path('practice/', main_views.practice, name='the-practice'),
    path('nrg-cleansing/', main_views.cleansing, name='nrg-cleansing'),
    path('nrg-massage/', main_views.massage, name='nrg-massage'),
    path('admin/', admin.site.urls),
    path('profile/', include('user_profile.urls')),
    path('', include('authentication.urls')),
    path('blog/', include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
