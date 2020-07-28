from templater import render


class IndexView:
    def __call__(self, request):
        template_name = "index.html"
        cities = [{'city': 'Москва'}, {'city': 'Санкт-Петербург'}]
        template = render(template_name, cities=cities)
        return '200 OK', template


class About:
    def __call__(self, request):
        template_name = 'about.html'
        authors = [
            {'author': 'Иван Иванов'},
            {'author': 'Петр Петров'},
            {'author': 'Сергей Сергеев'}
        ]
        template = render(template_name, authors=authors)
        return '200 OK', template


class Contacts:
    def __call__(self, request):
        template_name = 'contacts.html'
        addresses = [
            'Москва, ул. Тверская, 13',
            'Санкт-Петербург, Невский пр., 13',
            'Екатеринбург, ул. Мамина-Сибиряка, 13'
        ]
        template = render(template_name, addresses=addresses)
        return '200 OK', template
