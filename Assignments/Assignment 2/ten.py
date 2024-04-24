def addition(cnt):
    n=0
    while(cnt>0):
        n+=cnt%10
        cnt=cnt//10
    return n

def main():
    A=int(input("Enter the number: "))
    Ans=addition(A)
    print(Ans)

if __name__ == "__main__":
    main()