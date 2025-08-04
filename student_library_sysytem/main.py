class Library:
    
    def __init__(self,ListOfBooks):
        self.books = ListOfBooks
        
    def displayAvailableBooks(self):    
       print("Books present in this library are:")
       for books in self.books:
           print("\t" + books )
        

    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. please keep it safe and return it in 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry,This book has already been issued to someone else.please wait until the book is returened")  
            return False 
            
    def returnbook(self,bookname):
        self.books.append(bookname) 
        print("Thanks for returning this book! hope you enjoyed reading !")
        
                

class Student:
    
    def requestbook(self):
        book = input("enter the name of book you want to borrow")
        return book
    
    def returnbook(self):
        self.book = input("enter the name of book you want to return")
        return self.book
    
    
if __name__ == "__main__":
    centralLibrary = Library(["Algorithum","django","clrs","python "])
    #centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
       
        WelcomeMsg = '''======Welcome to central library======
        please choose an option
        1.list all the books
        2.request a book
        3.return a book
        4.exit the library
        '''
        print(WelcomeMsg)
        
        a= int(input("Enter a choose: "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            bookname = student.requestbook()
            centralLibrary.borrowBook(bookname)
        elif a==3 :
            bookname = student.returnbook()
            centralLibrary.returnbook(bookname)
        elif a==4 :
            print("Thanks for using central library! have a great day!")
            exit() 
            
        else:
            print("Invalid syntax")               
        
    
    
    