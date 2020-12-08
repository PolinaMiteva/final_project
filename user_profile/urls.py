from django.urls import path
from user_profile import views

urlpatterns = [
    # path('details/<int:pk>', views.DetailView.as_view(), name='details'),
    path('details/<int:pk>', views.details, name='details'),
    path('update/<int:pk>', views.update_profile, name='update-profile'),
]