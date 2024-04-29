stri = ""
def pattern(no):
    global stri
    if no == 0:
        return
    else:
        stri+="* "
        no = no - 1
        pattern(no)

def main():
    n=int(input("Enter the number: "))
    pattern(n)
    print(stri)

if __name__ == "__main__":
    main()