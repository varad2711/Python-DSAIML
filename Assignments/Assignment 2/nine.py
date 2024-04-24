def digits(cnt):
    n=0
    while(cnt>0):
        n+=1
        cnt=cnt//10
    return n

def main():
    A=int(input("Enter the number: "))
    Ans=digits(A)
    print(Ans)

if __name__ == "__main__":
    main()