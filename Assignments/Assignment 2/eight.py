def pattern(cnt):
    for i in range(1,cnt+1):
        for j in range(1,i+1):
            print(j, end =" ")
        print()


def main():
    no=int(input("Enter the number: "))
    pattern(no)

if __name__ == "__main__":
    main()