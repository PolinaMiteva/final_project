from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication.views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='log_in.html'), name='login'),
    # path('<int:pk>/update/', RegisterProfileView(), name='update profile'),
    # path('<int:pk>/update/', DeleteProfileView.as_view(), name='delete profile')

]
