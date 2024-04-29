i=1

def DisplayR(no):
    global i

    if(i<=no):
        print(i)
        i=i+1
        DisplayR(no)

def main():
    val=int(input("Enter the number: "))
    DisplayR(val)

if __name__=="__main__":
    main()