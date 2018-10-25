#从flask这个框架导入Flask这个类
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '我是第一个flask程序'


@app.route('/article/<id>')
def article(id):
    return '您请求的参数是: %s' % id


if __name__ == '__main__':
    app.run(debug=True)
