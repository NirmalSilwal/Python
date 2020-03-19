class Animal(object):

    def __init__(self):
        print('ANIMAL CREATED')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('EATING')


class Dog(Animal):
    # inheritance example
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def bark(self):
        print('bhauu bahuu!')

    def eat(self):
        # method overriding
        print('dog eating')


# animal = Animal()  # this invokes __init__() method
# animal.whoAmI()
# animal.eat()

dogie = Dog()
dogie.whoAmI()
dogie.eat()
dogie.bark()