def say_hello(func):
    print("Hello")
    func()

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hello(say_hi)
say_hello(say_bye)