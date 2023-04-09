from django.http.response import StreamingHttpResponse
from django.shortcuts import render


def gen_message(msg):
    return f'data: {msg} '


def iterator():
    for i in range(100000):
        yield gen_message(f'iteration {i}')


def test_stream(request):
    stream = iterator()
    response = StreamingHttpResponse(stream, status=200, content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response


def home(request):
    return render(request, 'stream/index.html')
