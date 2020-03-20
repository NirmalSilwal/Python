name = 'GLOBAL VARIABLE'


def scope_func():
    print('before initializing/assigning any local variables: ',locals())
    pages = 10
    print('after local variable declaration and assignment')
    print(locals()) # returns dictionary containing all local variable
    print('inside function name is : ', name)


scope_func()
print('outside function name is : ', name)
print('\nall global varibles: ')
print(globals())
