def say_hello(hello_var):
    print(hello_var)

    def say_hi(hi_var):
        print(hello_var + " " + hi_var)

    return say_hi


say_hi_func = say_hello("Hello")  # Print Hello and returns say_hi function which gets stored in say_hi_func variable

say_hi_func("Hi")  # Call say_hi function and print "Hello Hi"