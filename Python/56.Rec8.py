

def DisplayR(no):
    global i

    if(no >= 1):
        print(no)
        no=no-1
        DisplayR(no)

def main():
    val=int(input("Enter the number: "))
    DisplayR(val)

if __name__=="__main__":
    main()