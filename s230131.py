""" def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')
    return wrapper

@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요 {name}님!')
@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')
    
def emoji_hello(name, func):
    func(name)
    print('^~^//')
    

ko_hello('name')
en_hello('name')

 """
 
class MyClass:
    
    def method(self):
        return 'instance medthod'
    
    @classmethod
    def class_method(cls):
        return 'class method'
    
    @staticmethod
    def static_method():
        return 'static method'
    
my_class = MyClass()
print(my_class.method())
print(my_class.class_method())
print(my_class.static_method())