def say_hello():
    print("Hello")
    def say_hi():
        print("Hi")
    return say_hi


say_hi_func = say_hello() 

say_hi_func()