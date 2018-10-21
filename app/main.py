import json
import time
from wsgiref.util import request_uri

def wsgi_application(environ, start_response):
    # бизнес-логика
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html')
    ]
    data = {
    	"time": time.ctime(),
    	"url": request_uri(environ)
	}
    html_code = json.dumps(data)
    body = html_code.encode('utf-8')
    start_response(status, headers)
    return [ body ]

