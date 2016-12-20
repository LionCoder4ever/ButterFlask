
#*args

def test(f_arg, *args):
    print("first normal arg:",f_arg)
    for arg in args:
        print("another arg through *args :",arg)

# test('first param','python','java','ruby')

#**kwargs
#pass k-v into params

def test_kwargs(**kwargs):
    for k,v in kwargs.items():
        print("{0} <==> {1}".format(k,v))

# test_kwargs(name='python',another_name='ruby',first_name='java')

#*args and **kwargs
def test_args_and_kwargs(f_arg,*args,**kwargs):
    pass

def generator_function():
    for i in range(10):
        yield i

def fibo(n):
    a = b = 1
    for i in range(n):
        yield a            #迭代出的结果是a
        a,b = b,a+b        #模拟fibonacci

# for item in generator_function():
#     print(item)

# for item in fibo(20):
#     print(item)

#map(func, *iterables)
items = [1,2,3,4]

squared = list(map(lambda x:x**2, items))
print(squared)

def multi(x):
    return x*x
def plus(x):
    return x*2

funccollection = [multi,plus]

for i in range(5):
    newsquared = list(map(lambda x: x(i), funccollection))
    print(newsquared)

num_list = range(-5,5)
num_less_zero = list(filter(lambda x:x<0,num_list))
print(num_less_zero)

