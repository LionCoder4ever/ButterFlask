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
