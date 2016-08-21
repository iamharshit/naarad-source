import json
from django.utils.encoding import smart_str
from jinja2 import Template


def fixnewlines(data):
    for post in data:
        if 'message' in post:
            post['message'] = post['message'].replace('\n', '<br>')
    return data


def get_html(data):
    template_raw = open('feed.tmpl', 'r').read()
    template = Template(template_raw)
    data = fixnewlines(data)
    html = template.render(data=data)
    return smart_str(html)


def write_html(data, file_name):
    html = get_html(data)
    file_handle = open(file_name, 'w')
    file_handle.write(html)


if __name__ == "__main__":
    data = json.load(open('docs/feed.json', 'r'))

    write_html(data, 'docs/index.html')
