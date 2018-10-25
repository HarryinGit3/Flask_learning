#从flask这个框架导入Flask这个类
from flask import Flask,url_for
app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('my_list'))
    print(url_for('article',id ='123'))
    return '我是第一个flask程序'

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/article_love/<id>')
def article(id):
    return '您请求的参数是: %s' % id

if __name__ == '__main__':
    app.run(debug=True)
