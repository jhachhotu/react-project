from django.urls import path
from .views import api_home,  register, login, user_profile

urlpatterns = [
     path('', api_home, name='api_home'), 
    path('api/register/', register, name='register'),
    path('api/login/', login, name='login'),
    path('api/user-profile/<int:user_id>/', user_profile, name='user_profile'),
]
