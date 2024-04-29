def maxf(num1):
    max = num1[0]
    for no in num1:
        if(no>max):
            max=no

    return max

def main():
    num=[]
    N=int(input("Enter the number of elements N: "))

    print("Enter the elements: ")
    for i in range (0,N):
        num.append(int(input()))
    
    print("Maximum: ",max(num))

if __name__ == "__main__":
    main()