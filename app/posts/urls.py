from django.conf.urls import url
from . import views as post_view

urlpatterns = [
    url(r'^$', post_view.posts_list, name='home'),
    url(r'^create/$', post_view.posts_create, name='create'),
    url(r'^details/$', post_view.posts_detail, name='details'),
    url(r'^update$', post_view.posts_update, name='update'),
    url(r'^delete/$', post_view.posts_delete, name='delete'),
]
