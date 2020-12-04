from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Django_fnl_project import views as main_views
# from authentication import views as authentication_views
# from django.contrib.auth import views as contrib_auth_views
from Django_fnl_project import settings

urlpatterns = [
    path('', main_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('profile/', include('user_profile.urls')),
    path('', include('authentication.urls')),
    path('blog/', include('blog.urls')),
]

# urlpatterns = [
#     path('', main_views.index, name='index'),
#     path('admin/', admin.site.urls),
#     path('register/', authentication_views.register, name='register'),
#     path('login/', contrib_auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', authentication_views.logout_user, name='logout'),
#     path('profile/', include('user_profile.urls')),
# ]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
