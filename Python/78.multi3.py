
def DisplayEven(No):
    print("List of even numbers: ")
    x=2
    for i in range(No):
        print(x)
        x=x+2

def DisplayOdd(No):
    print("List of odd numbers: ")
    x=1
    for i in range(No):
        print(x)
        x=x+2

def main():
    Value=int(input("Enter number: "))
    DisplayEven(Value)
    DisplayOdd(Value)

if __name__ == "__main__":
    main()