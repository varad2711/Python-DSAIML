print("Demonstration of Procedural")

def Addition(No1,No2):
    Ans=No1+No2
    return Ans

def Substraction(No1,No2):
    Ans=No1-No2
    return Ans

def main():
    print("Enter first number")
    A=int(input())

    print("Enter second number")
    B=int(input())

    Ans=Addition(A,B)
    print("Addition is",Ans)

    Ans=Substraction(A,B)
    print("Substraction is",Ans)

if __name__ == "__main__":
    main()
