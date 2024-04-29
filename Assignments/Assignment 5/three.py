stri = ""
def pattern(no):
    global stri
    if no == 0:
        return
    else:
        stri+=str(no) + " "
        no = no - 1
        pattern(no)
    return stri

def main():
    n=int(input("Enter the number: "))
    print(pattern(n))

if __name__ == "__main__":
    main()