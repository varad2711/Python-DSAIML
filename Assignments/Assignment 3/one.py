def add(num1):
    sum=0
    for no in num1:
        sum+=no
    return sum

def main():
    num=[]
    N=int(input("Enter the number of elements N: "))
    print("Enter the elements: ")
    for i in range (0,N):
        num.append(int(input()))
    print("Addition: ",add(num))

if __name__ == "__main__":
    main()