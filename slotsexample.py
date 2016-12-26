# __slots__function helpful to reduce the memory

class MyClass(object):
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.function()

class NewClass(object):
    __slots__ = ['name','password']
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.function()






