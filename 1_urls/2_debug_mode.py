from flask import Flask
import config

app =Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    a =1
    b=0
    c=a/b
    return '我是第一个flask程序'

if __name__ =='__main__':
    app.run()