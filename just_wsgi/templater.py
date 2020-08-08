from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    # with open(template_name, encoding='utf-8') as t:
    #     template = Template(t.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    output_test = render('index.html', object_list=[{'city': 'Москва'}, {'city': 'Санкт-Петербург'}])
    print(output_test)
