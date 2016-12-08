from flask import Flask
from flask import current_app
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired




app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

#form protect
app.config['SECRET_KEY'] = 'secret salt'


class NameForm(Form):
    name = StringField("what's your name",validators=[DataRequired])
    submit = SubmitField('Submit')


@app.route('/')
def hello_index():

    return render_template('base.html',current_time=datetime.utcnow())


@app.route('/url')
def hello_world():
    print(app.url_map)
    return '<h1>Hello tet!<h1>'


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
def hello_redirect():
    return redirect('www.baidu.com')


@app.route('/jinjaname/<name>')
def hello_jinja(name):
    realurl = url_for('hello_world',_external=True)
    return render_template('jinjaname.html',name=name,realurl=realurl,current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',current_time=datetime.utcnow())

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


#url_for() ,a nice way to decouple


