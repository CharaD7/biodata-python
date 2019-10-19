# from django.urls import path
from django.conf.urls import url

from .views import *


app_name = 'test_app'

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^preview/$', preview, name = 'biodata'),
    url(r'^add_detail/$', add_detail, name = 'add_detail'),
    url(r'^edit_detail/(?P<pk>\d+)$', edit_detail, name = 'edit_detail'),
    url(r'^delete_detail/(?P<pk>\d+)$', delete_detail, name = 'delete_detail'),
    url(r'^upload_detail/$', upload_detail, name = 'upload_detail'),
]