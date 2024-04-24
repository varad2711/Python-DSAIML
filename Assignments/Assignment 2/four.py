def additions(cnt):
    Sum=0
    for i in range(1,cnt):
        if(cnt%i==0):
            Sum+=i
    return Sum

def main():
    A=int(input("Enter the number: "))
    Ans=additions(A)
    print(Ans)

if __name__ == "__main__":
    main()