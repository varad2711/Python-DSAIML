def prime(cnt):
    a=0
    if cnt<=1:
        print("Composite Number")
    if cnt == 2 or cnt == 3:
        print("Prime Number")
    for i in range (2,int(cnt**0.5)+1):
        if(cnt%i==0):
            print("Composite Number")
            a=1
    if(a==0):
        print("Prime Number")

def main():
    A=int(input("Enter the number: "))
    prime(A)

if __name__ == "__main__":
    main()