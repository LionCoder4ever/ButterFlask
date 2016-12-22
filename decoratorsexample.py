from functools import wraps
#function is also object

def f(name='coder'):
    def great():
        return 'now you in the great function'
    def welcome():
        return 'now you in the welcome function'
    if name == 'coder':
        return great
    else:
        return welcome

a = f()
print(a())


#pass function like a param

def hi():
    return 'hi'
def do_something(func):
    print('before')
    print(func())

do_something(hi)
print("********==**********")

#decorator:

def a_new_decorator(a_func):
        @wraps(a_func)
        def wrapTheFunction():
            print("before")
            a_func()
            print("after")
        return wrapTheFunction

@a_new_decorator
def a_function_require_decorator():
    print("i am the function added to the decorator")


print(a_function_require_decorator.__name__)
a_function_require_decorator()

#a usual example

def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "function will not run"
        return f(*args,**kwargs)
    return decorated

@decorator_name
def func():
    return "function is running"

can_run = False
print(func())


#authorization
def check_auth(f):
    @wraps(f)
    def function_need_auth(*args,**kwargs):
        if not 'auth' :
            pass
        return f(*args,**kwargs)
    return function_need_auth

#log
def log_i(f):
    @wraps(f)
    def function_called(*args,**kwargs):
        print(f.__name__+"was called")
        return f(*args,*kwargs)
    return function_called

@log_i
def my_func():
    print("my_func running")

my_func()

#log with the param
def log_it(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__+" was called"
            with open(logfile,'a') as openfile:
                openfile.write(log_string+'\n')
        return wrapped_function
    return logging_decorator
@log_it()
def my_func1():
    print("my_func1 running")

my_func1()

@log_it(logfile='newout.log')
def my_func2():
    print("my_func2 running")

my_func2()