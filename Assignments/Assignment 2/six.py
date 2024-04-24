def pattern(cnt):
    for i in range(cnt,0,-1):
        for j in range(0,i):
            print("* ", end =" ")
        print()


def main():
    no=int(input("Enter the number: "))
    pattern(no)

if __name__ == "__main__":
    main()