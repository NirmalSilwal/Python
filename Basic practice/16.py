class A:

    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)


class b(A):

    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

bb =  b('raj',33)
bb.display()
