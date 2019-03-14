def decorator_func(some_func):
    def wrapper_func():
        print("Wrapper function started")
        some_func()
        print("Wrapper function ended")
    return wrapper_func

def say_hello():
    print("Hello")

a = decorator_func(say_hello)
a()