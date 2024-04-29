def freqf(num1,f):
    freq=0
    for no in num1:
        if(no==f):
            freq+=1

    return freq

def main():
    num=[]
    N=int(input("Enter the number of elements N: "))

    print("Enter the elements: ")
    for i in range (0,N):
        num.append(int(input()))

    tof=int(input("Enter the number to find the frequency: "))

    print("Frequency: ",freqf(num,tof))

if __name__ == "__main__":
    main()