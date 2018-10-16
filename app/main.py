def wsgi_application(environ, start_response):
    # бизнес-логика
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html')
    ]
    html_code = """
    <html>
    <head>
    <meta charset="utf-8">
    <title>Boba Feta</title>
    </head>
    <body>
    <h1>Hello, Gunicorn!</h1>
    </body>
    </html>
    """
    body = html_code.encode('utf-8')
    start_response(status, headers)
    return [ body ]
