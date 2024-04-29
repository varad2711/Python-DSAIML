fac=1
def facto(no):
    global fac
    if no == 0 or no == 1:
        return 1
    fac =  no * facto(no - 1)
    
    return fac

def main():
    n=int(input("Enter the number: "))
    facto(n)
    print(fac)

if __name__ == "__main__":
    main()