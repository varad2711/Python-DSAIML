def pattern(cnt):
    for i in range(0,cnt):
        for i in range(0,cnt):
            print("* ", end =" ")
        print()


def main():
    no=int(input("Enter the number: "))
    pattern(no)

if __name__ == "__main__":
    main()