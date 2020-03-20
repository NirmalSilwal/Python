def new_decorator(func):

    def wrapper_func():
        print('code before executing func')
        func()
        print('func() has been called')

    return wrapper_func

@new_decorator
def func_needs_decorator():
    print('this function is in need of decorator!')


# func_needs_decorator()

# before adding @new_decorator

# decorator = new_decorator(func_needs_decorator)
# print(decorator)
# decorator()

# after adding @new_decorator

func_needs_decorator()