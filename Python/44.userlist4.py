def Addition(Data):
    Sum = 0

    for no in Data:
        Sum=Sum+no

    return Sum
    
def main():
    print("Enter number of lements that you want to insert in the list: ")
    size = int(input())

    Arr = list()

    print("Enter the elements: ")

    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are: ",Arr)
    
    Result = Addition(Arr)
    print("Summation of all the elements: ",Result)

if __name__ == "__main__":
    main()