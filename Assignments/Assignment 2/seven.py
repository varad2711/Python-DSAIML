def pattern(cnt):
    for i in range(1,cnt+1):
        for i in range(1,cnt+1):
            print(i, end =" ")
        print()


def main():
    no=int(input("Enter the number: "))
    pattern(no)

if __name__ == "__main__":
    main()