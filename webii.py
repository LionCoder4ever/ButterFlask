
#*args

def test(f_arg, *args):
    print("first normal arg:",f_arg)
    for arg in args:
        print("another arg through *args :",arg)

test('first param','python','java','ruby')

#**kwargs
#pass k-v into params

def test_kwargs(**kwargs):
    for k,v in kwargs.items():
        print("{0} <==> {1}".format(k,v))

test_kwargs(name='python',another_name='ruby',first_name='java')

#*args and **kwargs
def test_args_and_kwargs(f_arg,*args,**kwargs):
    pass





