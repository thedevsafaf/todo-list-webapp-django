from django.urls import re_path
from todolist_app import views

app_name = 'todolist_app'

urlpatterns = [
    re_path(r'^$', views.todolist, name='todolist'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit_task, name='edit_task'),
    re_path(r'^delete/(?P<id>\d+)/$', views.delete_task, name='delete_task'),
    re_path(r'^complete/(?P<id>\d+)/$',
            views.complete_task, name='complete_task'),
    re_path(r'^pending/(?P<id>\d+)/$',
            views.pending_task, name='pending_task'),
]
