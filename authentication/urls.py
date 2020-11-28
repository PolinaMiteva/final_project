from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login', template_name='login.html'), name='logout'),
    path('details/', views.profile_details, name='details'),
    path('update/', views.profile_update, name='update profile')

]