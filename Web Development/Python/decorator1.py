def hello():
    return 'hi'


def greet(func):
    print('hello welcome to my function')
    print(func)
    print(func())


greet(hello)
