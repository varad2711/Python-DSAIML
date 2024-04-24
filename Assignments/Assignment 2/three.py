def factorial(cnt):
    Ans=1
    for i in range (1,cnt+1):
        Ans=Ans*i
    return Ans

def main():
    A=int(input("Enter the number: "))
    Ans=factorial(A)
    print(Ans)

if __name__ == "__main__":
    main()