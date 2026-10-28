from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('user_details/<int:id>/', views.user_details, name='users'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('verification/', views.verify_user, name='verification')
]
