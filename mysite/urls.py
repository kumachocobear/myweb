from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse 

def home(request):
    return HttpResponse("Hello, this is home page!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video.urls')),
    path('', home),  
]
