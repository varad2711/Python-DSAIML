import threading

def EvenFactor(number):
    sum_even = 0
    for i in range(2, number + 1, 2):
        if number % i == 0:
            print(i)
            sum_even += i
    print("Sum of even factors of", number, ":", sum_even)

def OddFactor(number):
    sum_odd = 0
    for i in range(1, number + 1, 2):
        if number % i != 0:
            print(i)
            sum_odd += i
    print("Sum of odd factors of", number, ":", sum_odd)

def main():
    value = int(input("Enter a number: "))

    evenfactor = threading.Thread(target=EvenFactor, args=(value,))
    oddfactor = threading.Thread(target=OddFactor, args=(value,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
