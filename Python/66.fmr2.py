from functools import reduce

CheckEvenX=lambda No : No%2==0

IncreaseX=lambda No : No+1

AddX=lambda A,B : A+B

def main():
    Data=[11,14,20,23,18,16,15,20]
    print("Data from input list: ",Data)

    FData=list(filter(CheckEvenX,Data))           # should always have boolean value
    print("Data after filter activity: ",FData)

    MData=list(map(IncreaseX,FData))              # one input and one output
    print("Data after map activity: ",MData)

    RData=reduce(AddX,MData)                       # .
    print("Data after reduce activity: ",RData)

if __name__ == "__main__":
    main()