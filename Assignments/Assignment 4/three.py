from functools import reduce

def frange(no):
    if(no>=70 and no<=90):
        return True
    else:
        return False

frangeX = lambda no : no>=70 and no<=90

def add(no):
    return no+10

addX = lambda no : no+10

def product(A,B):
    return A*B

productX = lambda A,B : A*B

def main():
    data=[]
    N=int(input("Enter the number of elements N: "))

    print("Enter the elements: ")
    for i in range (0,N):
        data.append(int(input()))

    print("Data from input list: ", data)    

    fdata=list(filter(frangeX,data))
    print("Data after filter activity: ",fdata)

    mdata=list(map(addX,fdata))
    print("Data after map activity: ",mdata)

    rdata=reduce(productX,mdata)
    print("Data after reduce activity: ",rdata)

if __name__ == "__main__":
    main()