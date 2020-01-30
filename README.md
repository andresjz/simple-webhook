# Simple Webhook



Set the following variables

WEBHOOK_SECRET_KEY=The_Secret_key # Secret key to generate passwords
WEBHOOK_PORT=8888 # Running port change if necessary


Start server

pip install -r requirements.txt
python webhook.py

Current routes defined

/api/webhook/test -> This route is a simple example


Run client

Client help you to send request easily you just need to pass the path what of the hook, for instance:

python client.py /test params


you can also call a hook by itself using curl as follow

``` sh

$ curl -u token_generated:unused -i -X GET http://127.0.0.1:5000/api
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 30

{
  "data": "Hello, miguel!"
}

-u = Authorization: Basic base64
```
In this case we assume that you alredy have a token 


Future improvements

Security 



# Restarting with reloader
#app.run(debug=True, use_reloader=True)
