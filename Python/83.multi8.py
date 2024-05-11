import threading

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

    p1=threading.Thread(target=DisplayEven,args=(Value,)) # this comma is a placeholder for the tuple input
    p2=threading.Thread(target=DisplayOdd,args=(Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    print("End of main process")

if __name__ == "__main__":
    main()