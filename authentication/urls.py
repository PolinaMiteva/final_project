from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]