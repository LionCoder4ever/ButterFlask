# object mutability

foo = ['good']

bar = foo

bar+=['bye']

print(bar)
print(foo)


# list mutability
# be careful when def the *args

def add_to(num,target=[]):
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))