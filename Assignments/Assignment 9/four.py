import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python four.py <file1> <file2>")
        return
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if os.path.exists(file1) and os.path.exists(file2):
        fobj1 = open(file1, 'r')
        contents1 = fobj1.read()
        fobj1.close()

        fobj2 = open(file2, 'r')
        contents2 = fobj2.read()
        fobj2.close()

        if contents1 == contents2:
            print("Success")
        else:
            print("Failure")
    else:
        if not os.path.exists(file1):
            print("File 1 does not exist")
        if not os.path.exists(file2):
            print("File 2 does not exist")

if __name__ == "__main__":
    main()
