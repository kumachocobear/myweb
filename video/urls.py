from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^private_hls/(?P<filename>.+)$', views.hls_stream, name='hls_stream'),
]
