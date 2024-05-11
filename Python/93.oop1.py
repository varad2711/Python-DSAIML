
class Demo:
    Data1 = 11
    Data2 = 21

    def __init__(self, A, B):
        print("Inside Constructor")
        self.No1 = A
        self.No2 = B

    def Display(self):
        print()
        print("Value of No1 from display: ",self.No1)
        print("Value of No2 from display: ",self.No2)
        print("Value of Data1 from display: ",Demo.Data1)
        print("Value of Data2 from display: ",Demo.Data2)

obj1 = Demo(5,10)

obj2 = Demo(15,20)

print("Value of No1 from obj1: ",obj1.No1)
print("Value of No2 from obj1: ",obj1.No2)

print("Value of No1 from obj2: ",obj2.No1)
print("Value of No2 from obj2: ",obj2.No2)

print("Value of Data1: ",Demo.Data1)
print("Value of Data2: ",Demo.Data2)

obj1.Display()
obj2.Display()