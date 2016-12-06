from flask import Flask
from flask import current_app
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(app.url_map)
    return '<h1>Hello World!<h1>'


@app.route('/user/<username>')
def hello_user(username):
    if  str.isupper(username):
        abort(404)
    return '<h1>hello,%s</h1>' % username


@app.route('/responce')
def hello_responce():
    response = make_response('<h1>come from responce</h1>')
    response.set_cookie('answer',42)
    return response


@app.route('/redirect')
def hello_redirect(username):
    return redirect('google.com',404)


#@app.before_first_request

if __name__ == '__main__':
    app.run()


#app.url_map the mapper for route and function : example
#   Map([<Rule '/' (GET, OPTIONS, HEAD) -> hello_world>,
#   <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>,
#   <Rule '/user/<username>' (GET, OPTIONS, HEAD) -> hello_user>])

#before_first_request:注册一个函数,在处理第一个请求之前运行。
#before_request:注册一个函数,在每次请求之前运行。
#after_request:注册一个函数,如果没有未处理的异常抛出,在每次请求之后运行
#teardown_request:注册一个函数,即使有未处理的异常抛出,也在每次请求之后运行。

#function:the second param is httpcode ,400

#you can also return the response

#abort(404) change the  control to server


