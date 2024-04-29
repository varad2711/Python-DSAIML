stri = ""
i=1
def pattern(no):
    global stri,i
    if i == no + 1:
        return
    else:
        stri+=str(i)+ " "
        i = i + 1
        pattern(no)

def main():
    n=int(input("Enter the number: "))
    pattern(n)
    print(stri)

if __name__ == "__main__":
    main()