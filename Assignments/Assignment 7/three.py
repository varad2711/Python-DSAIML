class Arithmatic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter First Value: "))
        self.Value2=int(input("Enter Second Value: "))

    def Addition(self):
        return self.Value1+self.Value2

    def Subtraction(self):
        return self.Value1-self.Value2

    def Multiplication(self):
        return self.Value1*self.Value2
    
    def Division(self):
        if(self.Value2==0):
            return "Can't"
        else:
            return self.Value1/self.Value2
    
obj1 = Arithmatic()
obj1.Accept()
print(obj1.Addition())
print(obj1.Subtraction())
print(obj1.Multiplication())
print(obj1.Division())


obj2 = Arithmatic()
obj2.Accept()
print(obj2.Addition())
print(obj2.Subtraction())
print(obj2.Multiplication())
print(obj2.Division())