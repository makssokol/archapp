from templater import render
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
        code, text = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        self.methods(environ)
        return [bytes(text, encoding='utf-8')]

    def methods(self, environ):
        method = environ['REQUEST_METHOD']
        if method == 'GET':
            query_string = environ['QUERY_STRING']
            data = self.parse_input_data(query_string)
            return data
        elif method == 'POST':
            bytes_data = self.get_post_data(environ)
            data = self.parse_post_data(bytes_data)
            self.requests_saver(data)

    def requests_saver(self, data):
        with open('post_requests.txt', 'a') as f:
            f.write(str(data) + '\n')

    def parse_input_data(self, data):
        result = {}
        if data:
            print(f'data in parse_input_data = {data}')
            data = data.split('&')
            for item in data:
                k, v = item.split('=')
                result[k] = v
        return result

    def get_post_data(self, environ):
        data = environ['wsgi.input'].read()
        print(f'in get post data data = {data}')
        return data

    def parse_post_data(self, data):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(f'data_str = {data_str}')
            result = self.parse_input_data(data_str)
            print(f'result in parse_post_data = {result}')
        return result



application = Application(routes, front_list)
