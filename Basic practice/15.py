class A:

    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)

a = A('www')
a.display()


class Complex:

    def __init__(self,real,img):
        self.real=real
        self.img=img

    def display(self):
        print(self.real,self.img)

c = Complex(3,4)
c.display()
