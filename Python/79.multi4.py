import multiprocessing

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

    p1=multiprocessing.Process(target=DisplayEven,args=(Value,))
    p2=multiprocessing.Process(target=DisplayOdd,args=(Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    print("End of main process")

if __name__ == "__main__":
    main()