class NotEqualError(Exception):
    pass
n1 =10
n2 =10
try:
    if n1 != n2:
        raise NotEqualError
    else:
        print('Equal')
except NotEqualError:
    print('NotEqualError')
