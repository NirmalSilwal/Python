value = 10


def printer():
    global value
    # now changing the value of global variable "value"
    value = 20


print('before function call value is: ',value)
printer(value)
print('after function call value is: ',value)
