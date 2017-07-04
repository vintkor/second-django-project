from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.blog_single_post, name='blog_single_post')
]