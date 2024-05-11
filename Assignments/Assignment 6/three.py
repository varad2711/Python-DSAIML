import threading

def AddEven(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    print("Sum of even elements:", even_sum)

def AddOdd(numbers):
    odd_sum = 0
    for num in numbers:
        if num % 2 != 0:
            odd_sum += num
    print("Sum of odd elements:", odd_sum)

def main():
    input_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]

    even_thread = threading.Thread(target=AddEven, args=(input_list,))
    odd_thread = threading.Thread(target=AddOdd, args=(input_list,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
