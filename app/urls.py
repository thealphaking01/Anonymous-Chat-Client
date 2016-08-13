from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chat/$', views.chat , name='chat'),
    url(r'^hit/$', views.hit , name='hit'),
    url(r'^sendText/$', views.sendText , name='sendText'),
    # url(r'^shared_playlists/$', views.shared_playlists , name='shared_playlists'),
    # url(r'^create_playlist/$', views.create_playlist , name='create_playlist'),
    # url(r'^my_playlists/$', views.my_playlists , name='my_playlists'),
    url(r'^connect/(?P<id>[0-9]+)$', views.connect , name='connect'),
]