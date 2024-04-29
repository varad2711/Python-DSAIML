import MarvellousNum as m
def ListPrime(list1):
    flist=[]
    for no in list1:
        if (m.ChkPrime(no)):
            flist.append(no)
    sum=0
    for no2 in flist:
        sum+=no2
    return sum,flist

def main():
    num=[]
    N=int(input("Enter the number of elements N: "))

    print("Enter the elements: ")
    for i in range (0,N):
        num.append(int(input()))
    list2=[]
    sum,list2=ListPrime(num)
    print("Output",sum,list2)



if __name__ == "__main__":
    main()