from django.urls import re_path, include
from users_app import views

app_name = 'users_app'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
]
