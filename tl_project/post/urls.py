from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('user_added/', views.upload_user, name='upload_user'),
    path('post_added/', views.upload_post, name='upload_post'),
]