import threading

def Display1to50():
    for i in range(1, 51):
        print("Thread1:", i)

def Display50to1():
    for i in range(50, 0, -1):
        print("Thread2:", i)

def main():
    thread1 = threading.Thread(target=Display1to50)
    thread2 = threading.Thread(target=Display50to1)

    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
