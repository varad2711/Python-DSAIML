def prime(cnt):
    n=0
    for i in range(1,cnt):
        if(cnt%i==0):
            n+=1
    if(n==1):
        print("It is a Prime Number")
    else:
        print("It is a Composite Number")

def main():
    A=int(input("Enter the number: "))
    prime(A)

if __name__ == "__main__":
    main()