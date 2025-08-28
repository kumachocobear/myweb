import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render

def index(request):
    return render(request, 'video/index.html')

def hls_stream(request, filename):
    file_path = os.path.join(settings.BASE_DIR, 'private_hls', filename)

    if not os.path.exists(file_path):
        raise Http404("File not found")

    if file_path.endswith('.m3u8'):
        content_type = 'application/vnd.apple.mpegurl'
    elif file_path.endswith('.ts'):
        content_type = 'video/MP2T'
    else:
        content_type = 'application/octet-stream'

    return FileResponse(open(file_path, 'rb'), content_type=content_type)
