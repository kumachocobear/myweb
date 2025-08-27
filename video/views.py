import os
from django.conf import settings
from django.http import StreamingHttpResponse, Http404
from django.shortcuts import render

def index(request):
    return render(request, 'video/index.html')


def stream_video(request):
    """
    Stream video with proper Range support for browsers
    """
    file_path = os.path.join(settings.BASE_DIR, 'video', 'static', 'video', 'sample.mp4')

    if not os.path.exists(file_path):
        raise Http404("Video not found")

    file_size = os.path.getsize(file_path)
    range_header = request.headers.get('Range', '').strip()
    start = 0
    end = file_size - 1

    if range_header:
        # ตัวอย่าง Range: "bytes=0-1023"
        try:
            bytes_range = range_header.replace('bytes=', '').split('-')
            if bytes_range[0]:
                start = int(bytes_range[0])
            if len(bytes_range) > 1 and bytes_range[1]:
                end = int(bytes_range[1])
        except ValueError:
            pass  # ถ้าแปลงไม่สำเร็จ ใช้ค่า default

    chunk_size = end - start + 1

    def file_iterator(path, offset, length, chunk=8192):
        with open(path, 'rb') as f:
            f.seek(offset)
            remaining = length
            while remaining > 0:
                read_length = min(chunk, remaining)
                data = f.read(read_length)
                if not data:
                    break
                yield data
                remaining -= len(data)

    response = StreamingHttpResponse(
        file_iterator(file_path, start, chunk_size),
        status=206 if range_header else 200,
        content_type='video/mp4'
    )
    response['Content-Length'] = str(chunk_size)
    response['Accept-Ranges'] = 'bytes'
    response['Content-Range'] = f'bytes {start}-{end}/{file_size}'

    return response
