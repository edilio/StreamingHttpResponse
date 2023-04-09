# StreamingHttpResponse
A sample of a django app sending a `StreamingHttpResponse` and handling that stream in `JS`

We don't need really db or models in this example so the code is under `apps/stream/views` and `apps/stream/templates/stream/index.html`

## How to use it

- run pip install django or poetry install
- run git clone git@github.com:edilio/StreamingHttpResponse.git
- run python manage.py runserver
- browse http://localhost:8000

You can look for 'start new chunk:' so you can see that data comes in several chunks

### Here is the view code. 
We are using an iterator, so you can replace it with your own long processing iterator

```python
from django.http.response import StreamingHttpResponse
from django.shortcuts import render


def gen_message(msg):
    return 'data: {}'.format(msg)


def iterator():
    for i in range(100000):
        yield gen_message('iteration ' + str(i))


def test_stream(request):
    stream = iterator()
    response = StreamingHttpResponse(stream, status=200, content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response


def home(request):
    return render(request, 'stream/index.html')
```
