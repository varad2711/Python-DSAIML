def minf(num1):
    min = num1[0]
    for no in num1:
        if(no<min):
            min=no

    return min

def main():
    num=[]
    N=int(input("Enter the number of elements N: "))

    print("Enter the elements: ")
    for i in range (0,N):
        num.append(int(input()))

    print("Minimum: ",minf(num))

if __name__ == "__main__":
    main()