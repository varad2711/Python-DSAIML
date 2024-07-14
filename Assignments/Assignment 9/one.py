import os

def main():
    print("Enter the name of file: ")
    Fname = input()

    if os.path.exists(Fname):
        print("File exist's")
        
    else:
        print("File does not exist's")


if __name__ == "__main__":
    main()