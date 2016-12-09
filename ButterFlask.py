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
from flask import session

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

from flask import flash

from flask_sqlalchemy import SQLAlchemy
import os



baseDir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


app.config['SQLALCHEMY_DATABASE_URI'] = \
'sqlite:///' + os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

#form protect
app.config['SECRET_KEY'] = 'secret salt'


class NameForm(FlaskForm):
    name = StringField("what's your name",validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/index')
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


@app.route('/',methods=['GET','POST'])
def hello_jinja():
    realurl = url_for('hello_world',_external=True)
    name = None
    form = NameForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = ''
    # if form.validate_on_submit():
    #     session['name'] = form.name.data
    #     redirect(url_for('hello_jinja'))
    if form.validate_on_submit():
        old_name = session.get('name1')
        if old_name is not None and old_name !=form.name.data:
            flash('you have changed your name!')
        session['name1']=form.name.data
        redirect(url_for('hello_jinja'))
    return render_template('jinjaname.html',form=form,name=session.get('name1'),realurl=realurl,current_time=datetime.utcnow())


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


