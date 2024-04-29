from functools import reduce

def feven(no):
    if(no%2==0):
        return True
    else:
        return False
    
def fsquare(no):
    return no**2

def fadd(A,B):
    return A+B

def main():
    data=[]
    N=int(input("Enter the number of elements N: "))

    print("Enter the elements: ")
    for i in range (0,N):
        data.append(int(input()))

    print("Data from input list: ", data)    

    fdata=list(filter(feven,data))
    print("Data after filter activity: ",fdata)

    mdata=list(map(fsquare,fdata))
    print("Data after map activity: ",mdata)

    rdata=reduce(fadd,mdata)
    print("Data after reduce activity: ",rdata)

if __name__ == "__main__":
    main()