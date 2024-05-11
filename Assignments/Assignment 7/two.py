class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0
        self.Area=0
        self.Circumference=0

    def Accept(self):
        self.Radius=int(input("Enter Radius: "))

    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius

    def Display(self):
        print("Radius: ",self.Radius)
        print("Area: ",self.Area)
        print("Circumference: ",self.Circumference)

obj1 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2 = Circle()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
