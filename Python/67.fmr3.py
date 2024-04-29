from functools import reduce

def main():
    Data=[11,14,20,23,18,16,15,20]
    print("Data from input list: ",Data)

    FData=list(filter((lambda No : No%2==0),Data))           # should always have boolean value
    print("Data after filter activity: ",FData)

    MData=list(map((lambda No : No+1),FData))              # one input and one output
    print("Data after map activity: ",MData)

    RData=reduce(lambda A,B : A+B,MData)                       # .
    print("Data after reduce activity: ",RData)

if __name__ == "__main__":
    main()