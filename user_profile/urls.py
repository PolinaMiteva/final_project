from django.urls import path
from user_profile import views

urlpatterns = [
    path('details/<int:pk>', views.Details.as_view(), name='details'),
    path('update/<int:id>', views.UpdateProfile.as_view(), name='update profile'),
]