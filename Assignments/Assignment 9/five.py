import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python five.py <filename> <string>")
        return
    
    filename = sys.argv[1]
    search_string = sys.argv[2]

    if os.path.exists(filename):
        fobj = open(filename, 'r')
        contents = fobj.read()
        fobj.close()

        frequency = contents.count(search_string)
        print("The string appears" ,frequency, "times in the file.")
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()
