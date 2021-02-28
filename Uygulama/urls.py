from django.conf.urls import url

from . import admin
from .views import *

urlpatterns = [

    url(r'^index/$', Uygulama_index),
    url(r'^detail/$', Uygulama_detail),
    url(r'^create/$', Uygulama_create),
    url(r'^update/$', Uygulama_update),
    url(r'^delete/$', Uygulama_delete),

]
