import threading

def Even():
    for i in range(2,21):
        if(i%2==0):
            print(i)

def Odd():
    for i in range(1,20):
        if(i%2!=0):
            print(i)

def main():
    even=threading.Thread(target=Even)
    odd=threading.Thread(target=Odd)

    even.start()
    odd.start()

    even.join()
    odd.join()

if __name__ == "__main__":
    main()