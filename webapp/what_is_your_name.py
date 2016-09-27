from flask import Flask, request
from jinja2 import Environment, PackageLoader

app = Flask(__name__)
env = Environment(autoescape=True, loader=PackageLoader('webapp', 'templates'))


@app.route('/', methods=['GET'])
def what_is_your_name():
    yourname = request.args.get('yourname')
    template = env.get_template('home.html')
    return template.render(yourname=yourname)


if __name__ == '__main__':
    app.run('0.0.0.0')
