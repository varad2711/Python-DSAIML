import psutil
import sys

def DisplayProcessInfo(Pname):
    for proc in psutil.process_iter(['pid' , 'name' , 'username']):
        if proc.name() == Pname:
            print(proc)

def main():
    DisplayProcessInfo(sys.argv[1])

if __name__ == "__main__":
    main()