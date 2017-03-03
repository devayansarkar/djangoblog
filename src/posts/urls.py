from django.conf.urls import url
from .views import(
posts_list,
posts_create,
posts_detail,
posts_update,
posts_delete
)

urlpatterns = [
    url(r'^$', posts_list, name='home'),
    url(r'^create/$', posts_create, name='create'),
    url(r'^(?P<id>\d+)/edit/$', posts_update, name='update'),
    url(r'^(?P<id>\d+)/$', posts_detail, name='details'),
    url(r'^delete/$', posts_delete, name='delete'),
]
