from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('change_pass/', views.ChangePassView.as_view(), name='change_pass'),
    path('pass_changed', views.PassChangedSuccess.as_view(), name='pass_change_success'),
    path('logout/', views.logout_user, name='logout'),
]