from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('private_hls/<str:filename>/', views.hls_stream, name='hls_stream'),
]
