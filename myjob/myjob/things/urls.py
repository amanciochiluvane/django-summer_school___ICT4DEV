from django.urls import include, path
from . import  views

urlpatterns = [
    path(r'^$',include(views.post_list) ),
    path(r'^post/(?P<pk>[0-9]+)/$',include(views.post_detail) ),
    path(r'^post/new/$',include(views.post_new) , name='post_new'),
]