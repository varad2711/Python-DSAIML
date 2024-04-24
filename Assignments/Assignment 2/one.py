import Arithmatic as ar

def main():
    print("Enter first number: ")
    A=int(input())

    print("Enter second number: ")
    B=int(input())

    Ans = ar.Add(A,B)
    print("Addition is : ",Ans)

    Ans = ar.Sub(A,B)
    print("Substraction is : ",Ans)

    Ans = ar.Mult(A,B)
    print("Multiplication is : ",Ans)

    Ans = ar.Div(A,B)
    print("Division is : ",Ans)


if __name__ == "__main__":
    main()