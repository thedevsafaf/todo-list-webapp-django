from django.contrib import admin
from django.urls import re_path, include
from todolist_app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^todolist/', include('todolist_app.urls', namespace='todolist')),
    re_path(r'^account/', include('users_app.urls', namespace='users_app')),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^about/$', views.about, name='about'),
]
