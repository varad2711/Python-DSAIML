import threading

def CountSmallChars(string):
    count = sum(1 for char in string if char.islower())
    print("Thread ID:", threading.get_ident(), "Thread Name:", threading.current_thread().name, "Number of small characters:", count)

def CountCapitalChars(string):
    count = sum(1 for char in string if char.isupper())
    print("Thread ID:", threading.get_ident(), "Thread Name:", threading.current_thread().name, "Number of capital characters:", count)

def CountDigits(string):
    count = sum(1 for char in string if char.isdigit())
    print("Thread ID:", threading.get_ident(), "Thread Name:", threading.current_thread().name, "Number of digits:", count)

def main():
    input_string = input("Enter a string: ")

    small_thread = threading.Thread(target=CountSmallChars, args=(input_string,))
    capital_thread = threading.Thread(target=CountCapitalChars, args=(input_string,))
    digits_thread = threading.Thread(target=CountDigits, args=(input_string,))

    small_thread.name = "SmallCharsThread"
    capital_thread.name = "CapitalCharsThread"
    digits_thread.name = "DigitsThread"

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
