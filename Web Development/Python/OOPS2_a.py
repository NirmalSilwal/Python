class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi* self.radius*self.radius

    def set_radius(self,new_radius):
        self.radius = new_radius


myc = Circle(3)
print(myc.pi)
print(myc.area())
print(myc.area)
myc.set_radius(12)
print(myc.radius)
