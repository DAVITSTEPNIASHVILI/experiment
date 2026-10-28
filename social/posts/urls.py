from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('likes/<int:id>/', views.likes, name='likes'),
    path('comments/<int:id>/', views.comment, name='comments')
]