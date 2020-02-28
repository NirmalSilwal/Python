def decorator_func(say_hello_func):
    def wrapper_func(hello_var, world_var):

        hello = "Hello, "

        world = "World"

        if not hello_var:
            hello_var = hello

        if not world_var:
            world_var = world

        return say_hello_func(hello_var, world_var)

    return wrapper_func


@decorator_func
def say_hello(hello_var, world_var):
    print(hello_var + " " + world_var)


say_hello("Hello", "")