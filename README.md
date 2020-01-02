# Simple Webhook

``` sh

Start server

    pip install -r requirements.txt
    python webhook.py
    # Running on http://127.0.0.1:5000/
    # Restarting with reloader
    #app.run(debug=True, use_reloader=True)


Generate token

    python client.py


$ curl -u token_generated:unused -i -X GET http://127.0.0.1:5000/api
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 30

{
  "data": "Hello, miguel!"
}

```

