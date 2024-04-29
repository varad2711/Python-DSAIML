from functools import reduce

def fprime(no):
    if no<=1:
        return False
    if no == 2 or no == 3:
        return True
    for i in range (2,int(no**0.5)+1):
        if(no%i==0):
            return False
    return True

def fmul(no):
    return no*2

def fmax(A,B):
    return max(A,B)

def main():
    data = []
    N=int(input("Enter the number of elements N: "))
    print("Enter the elements: ")
    for i in range (0,N):
        data.append(int(input()))

    print("Input List: ",data)

    fdata=list(filter(fprime,data))
    print("List after filter: ",fdata)

    mdata=list(map(fmul,fdata))
    print("List after map: ",mdata)

    rdata=reduce(fmax,mdata)
    print("Output of reduce: ",rdata)

if __name__=="__main__":
    main()
