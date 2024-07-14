import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python three.py <filename>")
        return
    
    Fname = sys.argv[1]

    if os.path.exists(Fname):
        print("File exists")
        fobj = open(Fname, 'r')
        contents = fobj.read()
        nobj = open('Demo.txt', 'w')
        nobj.write(contents)
        print("Contents copied to Demo.txt")
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()
