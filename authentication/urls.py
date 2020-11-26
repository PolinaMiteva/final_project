from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication.views import RegisterProfileView, DeleteProfileView

urlpatterns = [
    path('register/', RegisterProfileView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='log_in.html'), name='login'),
    path('<int:pk>/update/', RegisterProfileView.as_view(), name='update profile'),
    path('<int:pk>/update/', DeleteProfileView.as_view(), name='delete profile')

]
