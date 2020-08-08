from routes import routes
from front_contollers import front_list
from views import *



class Application:
    def __init__(self, routes, front_list):
        self.routes = routes
        self.front_list = front_list

    class NotFound404:
        def __call__(self, request):
            text = '404 Page Not Found'
            return '404 Not Found', text

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = path + '/'
        request = {}
        for front in self.front_list:
            front(request)
        if path in self.routes:
            view = self.routes[path]
        else:
            view = self.NotFound404()
        print(f'request = {request}')
        print(f'environ = {environ}')
        code, text = view(request, environ)
        start_response(code, [('Content-Type', 'text/html')])
        return [bytes(text, encoding='utf-8')]


application = Application(routes, front_list)
