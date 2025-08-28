import boto3
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'video/index.html')

def hls_stream(request, filename):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME
    )

    url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': settings.AWS_S3_BUCKET_NAME, 'Key': f'sample/{filename}'},
        ExpiresIn=300
    )

    return JsonResponse({'url': url})
