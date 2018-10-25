#从flask这个框架导入Flask这个类
from flask import Flask,redirect,url_for
app = Flask(__name__)


@app.route('/')
def index():
    login_url = url_for('login')
    return redirect('/login/')
    return '这是首页'

@app.route('/login/')
def login():
    return'这是登录界面'

@app.route('/question/<is_login>')
def question(is_login):
    if is_login == '1':
        return '这是发布问答页面'
    else:
        return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)