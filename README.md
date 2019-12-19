# Simple Webhook

``` sh
    pip install -r requirements.txt
    python api.py
    # Running on http://127.0.0.1:5000/
    # Restarting with reloader


$ curl -u youtoken:unused -i -X GET http://127.0.0.1:5000/api
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 30

{
  "data": "Hello, miguel!"
}

```

