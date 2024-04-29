summ = 0
def suma(n):
    global summ
    if n == 0:
        return 0
    summ=(n%10)+suma(int(n/10))

    return summ

def main():
    n=int(input("Enter the number: "))
    print(suma(n))

if __name__ == "__main__":
    main()