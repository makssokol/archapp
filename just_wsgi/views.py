from templater import render


class IndexView:
    def __call__(self, request, environ):
        template_name = "index.html"
        cities = [{'city': 'Москва'}, {'city': 'Санкт-Петербург'}]
        template = render(template_name, cities=cities)
        return '200 OK', template


class About:
    def __call__(self, request, environ):
        template_name = 'about.html'
        authors = [
            {'author': 'Иван Иванов'},
            {'author': 'Петр Петров'},
            {'author': 'Сергей Сергеев'}
        ]
        template = render(template_name, authors=authors)
        return '200 OK', template


class Contacts:
    def __call__(self, request, environ):
        template_name = 'contacts.html'
        print(f'template_name: {template_name}')
        addresses = [
            'Москва, ул. Тверская, 13',
            'Санкт-Петербург, Невский пр., 13',
            'Екатеринбург, ул. Мамина-Сибиряка, 13'
        ]
        method = environ['REQUEST_METHOD']
        print(f'method - {method}')
        if method:
            if method == 'GET':
                query_string = environ['QUERY_STRING']
                print(f'query_string - {query_string}')
                data = MethodsParser.parse_input_data(query_string)
                print(f'data - {data}')
            elif method == 'POST':
                bytes_data = MethodsParser.get_post_data(environ)
                data = MethodsParser.parse_post_data(bytes_data)
                MethodsParser.requests_saver(data)
            template = render(template_name, addresses=addresses)
            print(f'template_name - {template_name}')
            return '200 OK', template
        else:
            return '405 Method Not Allowed', 'Method Not Allowed'


class MethodsParser:
    @staticmethod
    def requests_saver(data):
        with open('post_requests.txt', 'a') as f:
            f.write(str(data) + '\n')

    @staticmethod
    def parse_input_data(data):
        result = {}
        if data:
            print(f'data in parse_input_data = {data}')
            data = data.split('&')
            for item in data:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_post_data(environ):
        data = environ['wsgi.input'].read()
        print(f'in get post data data = {data}')
        return data

    @staticmethod
    def parse_post_data(data):
        result = {}
        if data:
            # print(f'data in parse post data = {data}')
            # print(f'data type - {type(data)}')
            # q = bytes(data.replace('%', '=').replace("+", " "), 'UTF-8')
            # b = quopri.decodestring(q)
            # data_str = b.decode(encoding='utf-8')
            data_str = data.decode(encoding='utf-8')
            # print(f'data_str = {data_str}')
            result = MethodsParser.parse_input_data(data_str)
            # print(f'result in parse_post_data = {result}')
        return result
