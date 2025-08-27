from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video.urls')),  # หน้าเว็บหลักเข้าถึง index
]
