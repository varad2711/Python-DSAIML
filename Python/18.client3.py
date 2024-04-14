import marvellous as m

def main():
    print("Enter first number: ")
    A=int(input())

    print("Enter second number: ")
    B=int(input())

    Ans=m.Addition(A,B)
    print("Addition is: ",Ans)

    Ans=m.Multiplication(A,B)
    print("Multiplication is: ",Ans)

main()