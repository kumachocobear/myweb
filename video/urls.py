from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # หน้า HTML
    path('stream/', views.stream_video, name='stream_video'),  # ส่งวิดีโอ
]
