class CoreApp:
    def __init__(self, urls, front_controllers):
        self.urls = urls
        self.front = front_controllers

    def __call__(self, environ, start_response):
        print('=================WORK=================')
        path = environ['PATH_INFO']
        if path in self.urls:
            view = self.urls[path]
            request = {}
            for controller in self.front:
                controller(request)
            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]
