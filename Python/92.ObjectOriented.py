print("Demonstration of Functional")

class Arithmatic:
    def __init__(self,Value1,Value2):
        self.No1=Value1
        self.No2=Value2

    def Addition(self):
        Ans=self.No1+self.No2
        return Ans

    def Substraction(self):
        Ans=self.No1-self.No2
        return Ans

print("Enter first number")
A=int(input())

print("Enter second number")
B=int(input())

obj = Arithmatic(A,B)

Ans=obj.Addition()
print("Addition is",Ans)

Ans=obj.Substraction()
print("Substraction is",Ans)

