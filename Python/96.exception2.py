def main():
    Ans = 0        
    print("Enter first number: ")
    No1=int(input())
    print("Enter second number: ")
    No2=int(input())
    try:
        Ans = No1 / No2

    except ZeroDivisionError as zobj:
        print("Exception occured",zobj)
        
    print("Division is: ",Ans)
    

if __name__ == "__main__":
    main()