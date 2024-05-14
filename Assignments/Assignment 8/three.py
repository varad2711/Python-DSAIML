class Numbers:
    def __init__ (self , No):
        self.No = No

    def ChkPerfect(self):
        Ans = 0
        for i in range(self.No-1 , 0 , -1):
            if(self.No%i==0):
                Ans = Ans + i
        if Ans == self.No:
            print("Perfect")
        else:
            print("Not perfect")

    def ChkPrime(self):
            a=0
            if self.No<=1:
                print("Composite Number")
            if self.No == 2 or self.No == 3:
                print("Prime Number")
            for i in range (2,int(self.No**0.5)+1):
                if(self.No%i==0):
                    print("Composite Number")
                    a=1
            if(a==0):
                print("Prime Number")

    def Factors(self):
        print("Factors : ")
        for i in range(self.No , 0 , -1):
            if(self.No%i==0):
                print(i , end=" ")
        print()

    def SumFactors(self):
        print("Factors : ")
        Ans = 0
        for i in range(self.No , 0 , -1):
            if(self.No%i==0):
                Ans = Ans + i
        print(Ans)


obj = Numbers(5)
obj.ChkPerfect()
obj.ChkPrime()
obj.Factors()
obj.SumFactors()