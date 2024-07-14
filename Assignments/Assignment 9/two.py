import os

def main():
    print("Enter the name of file: ")
    Fname = input()

    if os.path.exists(Fname):
        print("File exists")
        fobj= open(Fname, 'r')
        contents = fobj.read()
        print("Contents of the file:")
        print(contents)
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()
