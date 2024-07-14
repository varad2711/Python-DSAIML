import psutil

def DisplayProcessInfo():
    print("List of running processess are : ")
    print("_________________________________________________________")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)
    print("_________________________________________________________")

def main():
    DisplayProcessInfo()

if __name__ == "__main__":
    main()