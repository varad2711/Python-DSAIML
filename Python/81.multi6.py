import multiprocessing
import os
import threading

def DisplayEven(No):
    print("PID of even process",os.getpid())
    print("List of even numbers: ")
    x=2
    for i in range(No):
        print(x)
        x=x+2

def DisplayOdd(No):
    print("PID of odd process",os.getpid())
    print("List of odd numbers: ")
    x=1
    for i in range(No):
        print(x)
        x=x+2

def main():
    print("PID of main process",os.getpid())

    Value=int(input("Enter number: "))

    p1=multiprocessing.Process(target=DisplayEven,args=(Value,))
    p2=multiprocessing.Process(target=DisplayOdd,args=(Value,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
    
    print("End of main process")

if __name__ == "__main__":
    main()