from django.http.response import StreamingHttpResponse
from django.shortcuts import render


def gen_message(msg):
    return 'data: {}\n\n'.format(msg)


def iterator():
    for i in range(1000):
        yield gen_message('iteration ' + str(i))


def test_stream(request):
    stream = iterator()
    response = StreamingHttpResponse(stream, status=200, content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response


def home(request):
    return render(request, 'stream/index.html')