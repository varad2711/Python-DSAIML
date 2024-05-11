class BookStore:
    NoOfBooks=0

    def __init__(self):
        self.Name=str(input("Enter the Name: "))
        self.Author=str(input("Enter the Author: "))
        BookStore.NoOfBooks+=1

    def Display(self):
        print(self.Name,"by",self.Author,".","No of Books: ",BookStore.NoOfBooks)

obj1 = BookStore()
obj1.Display()

obj2 = BookStore()
obj2.Display()