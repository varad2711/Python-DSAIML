class BankAccount:
    ROI=10.5

    def __init__(self):
        self.Name=str(input("Enter the Name: "))
        self.Amount=int(input("Enter the Amount Number: "))
    
    def Display(self):
        print("Name: ",self.Name)
        print("Amount: ",self.Amount)

    def Deposit(self):
        dpt=int(input("Enter the Deposit amount: "))
        self.Amount+=dpt

    def Withdraw(self):
        wdt=int(input("Enter the Withdrawal amount: "))
        self.Withdraw-=wdt

    def CalculateInterest(self):
        interest=self.Amount*(10.5/100)