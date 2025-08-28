import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render

def index(request):
    return render(request, 'video/index.html')


def hls_stream(request, filename):

    base_path = os.path.join(settings.BASE_DIR, 'private_hls')
    file_path = os.path.join(base_path, filename)

    if not os.path.exists(file_path):
        raise Http404("File not found")

    if filename.endswith('.m3u8'):
        content_type = 'application/vnd.apple.mpegurl'
    elif filename.endswith('.ts'):
        content_type = 'video/MP2T'
    else:
        content_type = 'application/octet-stream'

    return FileResponse(open(file_path, 'rb'), content_type=content_type)
