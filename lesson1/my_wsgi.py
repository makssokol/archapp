from templater import render

object_list = [{'city': 'Москва'}, {'city': 'Санкт-Петербург'}]

class Application:
    def __init__(self, routes, front_list):
        self.routes = routes
        self.front_list = front_list

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        request = {}
        for front in self.front_list:
            front(request)
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFound404(request)
        code, text = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return text


class IndexView:
    def __call__(self, request):
        template = render("index.html", object_list=object_list)
        return '200 OK', [bytes(template, encoding='utf-8')]


class About:
    def __call__(self, request):
        return '200 OK', [b'about info']


class Contacts:
    def __call__(self, request):
        return '200 OK', [b'contacts info']


class NotFound404:
    def __call__(self, request):
        return '404 Not Found', [b'404 Page Not Found']


routes = {
    '/': IndexView(),
    '/about': About(),
    '/contacts': Contacts(),
}


def funny_front(request):
    request['funny'] = ':)))))'


def sad_front(request):
    request['sad'] = ':((((('


front_list = [funny_front, sad_front]

application = Application(routes, front_list)
