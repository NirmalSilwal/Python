class Dog():

    # Class object attribute
    species = 'mammalia'

    def __init__(self, breed,name):
        """
        I am called automatically whenever object of Dog class is created
        """
        self.breed = breed
        self.name = name

#
# dogie = Dog('lab')
# other_dog = Dog('Huskie')
# # print(type(dogie))
# print(dogie.breed)  # here breed is an attribute
# print(other_dog.breed)


new_dog = Dog('lab','kutta')
print(new_dog.breed,new_dog.name)
print(new_dog.species)
