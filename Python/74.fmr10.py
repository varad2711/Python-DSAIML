from marvellousfmr import *

def main():
    Data= []
    len=int(input("Enter the size of list: "))
    for i in range (0,len):
        Data.append(int(input()))
        
    print("Data from input list: ",Data)

    FData=list(filterX(CheckEven,Data))           # should always have boolean value
    print("Data after filter activity: ",FData)

    MData=list(mapX(Increase,FData))              # one input and one output
    print("Data after map activity: ",MData)

    RData=reduceX(Add,MData)                       # two input and one output
    print("Data after reduce activity: ",RData)

if __name__ == "__main__":
    main()