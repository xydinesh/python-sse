# python-sse
Testing out server sent events with python

## Installation
```
pip install -r requirements.txt
```

## Server

```
export FLASK_APP=sse
export FLASK_ENV=development
flask run
```

## Server-sent Events

Specify seconds to sleep before sending response to client. Default is 10 seconds.

```
curl "http://127.0.0.1:5000/datetime?sleep=3"
```
